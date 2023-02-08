import mysql.connector
from mysql.connector import Error
import configs
import logging
from telegram import KeyboardButton, ReplyKeyboardMarkup, Update
from telegram.ext import *
import redis
import re

float_pattern = re.compile("^(?:[1-9]\d*|0)?(?:\.\d+)?$")

ADD_SYMBOL = "add_symbol"
ADD_DIRECTION = "add_direction"
ADD_THRESHOLD = "add_threshold"
EXEC_ADD_COMMAND = "exec_add_command"

REMOVE_SYMBOL = "remove_symbol"
REMOVE_DIRECTION = "remove_direction"
REMOVE_INDICATOR = "remove_indicator"
UPDATE_THRESHOLD = "update_threshold"
EXEC_REMOVE_COMMAND = "exec_remove_command"

UPDATE_SYMBOL = "update_symbol"
UPDATE_DIRECTION = "update_direction"
UPDATE_INDICATOR = "update_indicator"
EXEC_UPDATE_COMMAND = "exec_update_command"

END_CONVERSATION = ConversationHandler.END

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

class Bot():
    def __init__(self) -> None:
        try:
            connection = mysql.connector.connect(
                host=configs.mysql_host,
                database=configs.mysql_database,
                port=configs.mysql_port,
                user=configs.mysql_username,
                password=configs.mysql_password
            )
            if connection.is_connected():
                self.connection = connection
                self.cursor = connection.cursor(buffered=True)
                self.cursor.execute("select database();")
                record = self.cursor.fetchone()
                print(f"Database connnected: {record}")
            else:
                print('No connect to mysql')
        except Error as e:
            logging.error("Error while connecting to MySQL:\n" + e)
        
        self.r = redis.Redis()
        logging.info("Connected to Redis")
        self.load_mysql_to_redis()

        add_conv_handler = ConversationHandler(
            entry_points=[CommandHandler("add", self.add_condition)],
            states={
                ADD_SYMBOL: [MessageHandler(filters.TEXT & ~filters.COMMAND, self.add_symbol),],
                ADD_DIRECTION:[MessageHandler(filters.TEXT & ~filters.COMMAND, self.add_direction),],
                ADD_THRESHOLD: [MessageHandler(filters.TEXT & ~filters.COMMAND, self.add_threshold),],
                EXEC_ADD_COMMAND: [MessageHandler(filters.TEXT & ~filters.COMMAND, self.exec_add_command),]
            },
            fallbacks=[CommandHandler("add", self.add_condition), CommandHandler("remove", self.remove_condition)]
        )

        remove_conv_handler = ConversationHandler(
            entry_points=[CommandHandler("remove", self.remove_condition)],
            states={
                REMOVE_SYMBOL: [MessageHandler(filters.TEXT & ~filters.COMMAND, self.remove_symbol),],
                REMOVE_INDICATOR:[ MessageHandler(filters.TEXT & ~filters.COMMAND, self.remove_indicator),],
                EXEC_REMOVE_COMMAND: [MessageHandler(filters.TEXT & ~filters.COMMAND, self.exec_remove_command),]
            },
            fallbacks=[CommandHandler("remove", self.remove_condition)]
        )

        update_conv_handler = ConversationHandler(
            entry_points=[CommandHandler("update", self.update_condition)],
            states={
                UPDATE_SYMBOL: [MessageHandler(filters.TEXT & ~filters.COMMAND, self.update_symbol),],
                UPDATE_INDICATOR:[ MessageHandler(filters.TEXT & ~filters.COMMAND, self.update_indicator),],
                UPDATE_THRESHOLD:[ MessageHandler(filters.TEXT & ~filters.COMMAND, self.update_threshold),],
                EXEC_UPDATE_COMMAND: [MessageHandler(filters.TEXT & ~filters.COMMAND, self.exec_update_command),]
            },
            fallbacks=[CommandHandler("update", self.update_condition)]
        )

        self.application = ApplicationBuilder().token(configs.TOKEN).build()
        
        self.application.add_handler(add_conv_handler, 1)
        self.application.add_handler(remove_conv_handler, 2)
        self.application.add_handler(update_conv_handler, 3)
        self.application.add_handler(CommandHandler('start', self.start), 0)
        self.application.add_handler(CommandHandler('help', self.help), 0)
        self.application.add_handler(CommandHandler('list', self.list_condition), 0)
        self.application.add_handler(CommandHandler('cancel', self.cancel), 0)
        self.application.add_handler(MessageHandler(filters.COMMAND & ~filters.Regex('^(\/add|\/start|\/list|\/remove|\/cancel|\/help|\/update|\/viewdata|\/predictdata)$'), self.command_unknown))

    def load_mysql_to_redis(self):
        self.r.flushall() # clear cache
        select_query = "SELECT * FROM stockalert"
        self.cursor.execute(select_query)
        conditions = self.cursor.fetchall()
        if conditions is None:
            return
        for condition in conditions:
            (chat_id, ticker, indicator, threshold, direction) = condition
            if direction == 0:
                self.r.zadd(f'alert:{indicator.upper()}:{ticker}:lt', {chat_id : threshold})
            else:
                self.r.zadd(f'alert:{indicator.upper()}:{ticker}:gt', {chat_id : threshold})

        
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        logging.info(f"Start command at chat: {str(chat_id)}")
        await context.bot.send_message(chat_id=chat_id, text=configs.WELCOME_MESSAGE)

    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        logging.info(f"Help command at chat: {str(chat_id)}")
        await context.bot.send_message(chat_id=chat_id, text=configs.HELP_MESSAGE)

    async def list_condition(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        logging.info(f"List condition command at chat: {str(chat_id)}")
        select_query = "SELECT * FROM stockalert WHERE chat_id = %s"
        self.cursor.execute(select_query, (str(chat_id),))
        rows = self.cursor.fetchall()
        
        if rows is None or len(rows) == 0: 
            message = configs.NO_CONDITION_MESSAGE
            logging.info(f"List condition at chat id {str(chat_id)}: Did not find any condition")
        else:
            message = "Your alert condition: \n"
            for row in rows:
                (chat_id, ticker, indicator, threshold, direction) = row
                message = message + "\nTicker " + ticker.upper()
                if direction == 0: 
                    message = message + f" has lower boundary on {indicator}: " + str(threshold)
                if direction == 1: 
                    message = message +  f" has upper boundary: {indicator}: " + str(threshold)
        await context.bot.send_message(chat_id=chat_id, text=message)
        logging.info(f"List condition at chat id {chat_id}: Success")

# ----------------------------------- start of add conversation------------------------------------------------------------
    async def add_condition(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        context.user_data.clear()
        context.user_data['command'] = "ADD"
        await update.message.reply_text("Select technical indicator to set condition on", 
                reply_markup=ReplyKeyboardMarkup(configs.ATTR_BUTTON, one_time_keyboard=True, resize_keyboard=True))
        return ADD_SYMBOL

    async def add_symbol(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        text = update.message.text
        if text.upper() in configs.ATTR:
            context.user_data['tech_indi'] = text.upper()
            await update.message.reply_text("Select the stock code to set condition on")
            return ADD_DIRECTION
        else:
            await update.message.reply_text("Sorry, I didn't understand this technical indicator yet :<\nTry some others", 
                reply_markup=ReplyKeyboardMarkup(configs.ATTR_BUTTON, one_time_keyboard=True, resize_keyboard=True))
            return ADD_SYMBOL

    async def add_direction(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        text = update.message.text
        if text.upper() in configs.TICKERS:
            context.user_data['symbol'] = text
            await update.message.reply_text("Select the direction to send alert: ",
                    reply_markup=ReplyKeyboardMarkup(configs.DIRECTION_BUTTON, one_time_keyboard=True, resize_keyboard=True))
            return ADD_THRESHOLD
        else:
            await update.message.reply_text("I am not support this stock yet :<\nTry some others")
            return ADD_DIRECTION

    async def add_threshold(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        text = update.message.text.strip().lower()
        ticker = context.user_data['symbol']
        indicator = context.user_data['tech_indi']
        chat_id = update.effective_chat.id
        if text== "greater than":
            context.user_data['direction'] = 1
            direction = 1
            select_query = "SELECT * FROM stockalert WHERE chat_id = %s and ticker = %s and indicator = %s and direction = %s"
            self.cursor.execute(select_query, (str(chat_id), ticker, indicator, direction))
            row = self.cursor.fetchone()
            if row is None:
                msg = f"Okay send alert when {context.user_data['tech_indi']} is {text} ... how much? Enter the threshold to complete the condition"
                await update.message.reply_text(msg)
                return EXEC_ADD_COMMAND
            else:
                msg = f"You have set this condition with threshold: {row[3]}"
                await context.bot.send_message(chat_id=chat_id, text=msg)
                return END_CONVERSATION
        elif text == "less than":
            context.user_data['direction'] = 0
            direction = 0
            select_query = "SELECT * FROM stockalert WHERE chat_id = %s and ticker = %s and indicator = %s and direction = %s"
            self.cursor.execute(select_query, (str(chat_id), ticker, indicator, direction))
            row = self.cursor.fetchone()
            if row is None:
                msg = f"Okay send alert when {context.user_data['tech_indi']} is {text} ... how much? Enter the threshold to complete the condition"
                await update.message.reply_text(msg)
                return EXEC_ADD_COMMAND
            else:
                msg = f"You have set this condition with threshold: {row[3]}"
                await context.bot.send_message(chat_id=chat_id, text=msg)
                return END_CONVERSATION
        else:
            await update.message.reply_text("Wrong direction! Please use the two button below or type in \"less than\"/\"greater than\" in the chat.",
                    reply_markup=ReplyKeyboardMarkup(configs.DIRECTION_BUTTON,  one_time_keyboard=True, resize_keyboard=True))
            return ADD_THRESHOLD

    async def exec_add_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        text = update.message.text
        if float_pattern.match(text):
            threshold = float(text)
            ticker = context.user_data['symbol'].upper()
            direction = context.user_data['direction']
            indicator = context.user_data['tech_indi'].upper()
            chat_id = update.effective_chat.id
            insert_query = f"INSERT INTO stockalert (chat_id, ticker, indicator, threshold, direction) values (%s, %s, %s, %s, %s)"
            self.cursor.execute(insert_query, (str(chat_id), ticker, indicator, threshold, direction))
            self.connection.commit()
            if direction == 1:
                self.r.zadd(f"{indicator}:{ticker}:gt", {chat_id: threshold})
            else:
                self.r.zadd(f"{indicator}:{ticker}:lt", {chat_id: threshold})
            message = "Alert added successfully! Use /list to see all your alert"
            logging.info(f"User added condition at chat id {chat_id}: Success -- Detail: {ticker} - {indicator} - {configs.DIRECTION_BUTTON[0][direction]} - {threshold}")
            await context.bot.send_message(chat_id=chat_id, text=message)
            return END_CONVERSATION
        else:
            await update.message.reply_text("I do not understand, the threshold should be a float number")
            return EXEC_ADD_COMMAND
# ------------------------------- end of add conversation ---------------------------------------------------


# ------------------------------- start of update conversation ---------------------------------------------
    async def update_condition(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        context.user_data.clear()
        context.user_data['command'] = 'UPDATE'
        chat_id = update.effective_chat.id
        select_query = "SELECT distinct ticker FROM stockalert WHERE chat_id = %s"
        self.cursor.execute(select_query, (str(chat_id),))
        rows = self.cursor.fetchall()
        if rows is None:
            await context.bot.send_message(chat_id=chat_id, text="You have not set up any condition yet.")
            return END_CONVERSATION
        else:
            context.user_data['list_symbol'] = []
            buttons = []
            b = []
            i = 0
            for row in rows:
                b.append(row[0])
                if len(b) == 3:
                    buttons.append(b)
                    b = []
                context.user_data['list_symbol'].append(row[0])
            if len(b) != 0:
                buttons.append(b)
            await update.message.reply_text("Which stock do you want to update condition",
                    reply_markup=ReplyKeyboardMarkup(buttons,  one_time_keyboard=True, resize_keyboard=True))
            return UPDATE_SYMBOL

    async def update_symbol(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        text = update.message.text.strip().upper()
        if text not in context.user_data['list_symbol']:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=f"You have not set up any condition on {text} yet.")
            return END_CONVERSATION
        else:
            context.user_data['symbol'] = text.upper()
            select_query = "SELECT distinct indicator FROM stockalert WHERE chat_id = %s and ticker = %s"
            self.cursor.execute(select_query, (str(update.effective_chat.id), text))
            rows = self.cursor.fetchall() 
            context.user_data['list_indi'] = []
            buttons = []
            b = []
            i = 0
            for row in rows:
                b.append(row[0])
                if len(b) == 3:
                    buttons.append(b)
                    b = []
                context.user_data['list_indi'].append(row[0])
            if len(b) != 0:
                buttons.append(b)
            await update.message.reply_text(f"Which indicator on {text.upper()} do you want to update condition",
                    reply_markup=ReplyKeyboardMarkup(buttons,  one_time_keyboard=True, resize_keyboard=True))
            return UPDATE_INDICATOR

    async def update_indicator(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        text = update.message.text.strip().upper()
        if text not in context.user_data['list_indi']:
            buttons = []
            b = []
            i = 0
            for indi in context.user_data['list_indi']:
                b.append(indi)
                if len(b) == 3:
                    buttons.append(b)
                    b = []
            if len(b) != 0:
                buttons.append(b)
            await update.message.reply_text(f"Hmm, Seems like {text.upper()} do not have condition on {text}. Try using buttons below", 
                    reply_markup=ReplyKeyboardMarkup(buttons,  one_time_keyboard=True, resize_keyboard=True))
            return UPDATE_INDICATOR
        context.user_data['tech_indi'] = text
        select_query = "SELECT distinct direction FROM stockalert WHERE chat_id = %s and ticker = %s and indicator = %s"
        self.cursor.execute(select_query, (update.effective_chat.id, context.user_data['symbol'], text))
        rows = self.cursor.fetchall()
        context.user_data['list_direction'] = []
        buttons = []
        b = []
        i = 0
        for row in rows:
            b.append(configs.DIRECTION_BUTTON[0][row[0]])
            if len(b) == 3:
                buttons.append(b)
                b = []
            context.user_data['list_direction'].append(configs.DIRECTION_BUTTON[0][row[0]])
        if len(b) != 0:
                buttons.append(b)
        await update.message.reply_text(f"Which direction on {text} of {context.user_data['symbol']} do you want to update condition", 
                reply_markup=ReplyKeyboardMarkup(buttons,  one_time_keyboard=True, resize_keyboard=True))
        return UPDATE_THRESHOLD

    async def update_threshold(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        text = update.message.text.strip()
        ticker = context.user_data['symbol']
        indicator = context.user_data['tech_indi']
        chat_id = update.effective_chat.id
        if text not in context.user_data['list_direction']:
            await update.message.reply_text("Seems like you have not set up condition like that! Please use the button(s) below or type in \"less than\"/\"greater than\" in the chat.",
                    reply_markup=ReplyKeyboardMarkup(configs.DIRECTION_BUTTON,  one_time_keyboard=True, resize_keyboard=True))
            return UPDATE_THRESHOLD
        if text == "greater than":
            context.user_data['direction'] = 1
        else:
            context.user_data['direction'] = 0
        msg = f"Finally, enter the threshold to complete the update process"
        await update.message.reply_text(msg)
        return EXEC_UPDATE_COMMAND
        
    async def exec_update_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        text = update.message.text.strip()
        if float_pattern.match(text):
            threshold = float(text)
            ticker = context.user_data['symbol'].upper()
            direction = context.user_data['direction']
            indicator = context.user_data['tech_indi'].upper()
            chat_id = update.effective_chat.id
            update_query = f"UPDATE stockalert set threshold = %s where chat_id = %s and ticker = %s and indicator = %s and direction = %s"
            self.cursor.execute(update_query, (threshold, str(chat_id), ticker, indicator, direction))
            self.connection.commit()
            if direction == 1:
                self.r.zrem(f"{indicator}:{ticker}:gt", chat_id)
                self.r.zadd(f"{indicator}:{ticker}:gt", {chat_id: threshold})
            else:
                self.r.zrem(f"{indicator}:{ticker}:lt", chat_id)
                self.r.zadd(f"{indicator}:{ticker}:lt", {chat_id: threshold})
            message = "Alert updated successfully! Use /list to see all your alert"
            logging.info(f"User updated condition at chat id {chat_id}: Success -- Detail: {ticker} - {indicator} - {configs.DIRECTION_BUTTON[0][direction]} - {threshold}")
            await context.bot.send_message(chat_id=chat_id, text=message)
            return END_CONVERSATION
        else:
            await update.message.reply_text("I do not understand, the threshold should be a float number")
            return EXEC_UPDATE_COMMAND
# ------------------------------- end of update conversation ---------------------------------------------------


# ------------------------------- start of remove conversation ---------------------------------------------
    async def remove_condition(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        context.user_data.clear()
        context.user_data['command'] = 'DELETE'
        chat_id = update.effective_chat.id
        select_query = "SELECT distinct ticker FROM stockalert WHERE chat_id = %s"
        self.cursor.execute(select_query, (str(chat_id),))
        rows = self.cursor.fetchall()
        if rows is None:
            await context.bot.send_message(chat_id=chat_id, text="You have not set up any condition yet.")
            return END_CONVERSATION
        else:
            context.user_data['list_symbol'] = []
            buttons = []
            b = []
            i = 0
            for row in rows:
                b.append(row[0])
                if len(b) == 3:
                    buttons.append(b)
                    b = []
                context.user_data['list_symbol'].append(row[0])
            if len(b) != 0:
                buttons.append(b)
            await update.message.reply_text("Which stock do you want to remove condition",
                    reply_markup=ReplyKeyboardMarkup(buttons,  one_time_keyboard=True, resize_keyboard=True))
            return REMOVE_SYMBOL

    async def remove_symbol(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        text = update.message.text.strip().upper()
        if text not in context.user_data['list_symbol']:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=f"You have not set up any condition on {text} yet.")
            return END_CONVERSATION
        else:
            context.user_data['symbol'] = text.upper()
            select_query = "SELECT distinct indicator FROM stockalert WHERE chat_id = %s and ticker = %s"
            self.cursor.execute(select_query, (str(update.effective_chat.id), text))
            rows = self.cursor.fetchall() 
            context.user_data['list_indi'] = []
            buttons = []
            b = []
            i = 0
            for row in rows:
                b.append(row[0])
                if len(b) == 3:
                    buttons.append(b)
                    b = []
                context.user_data['list_indi'].append(row[0])
            if len(b) != 0:
                buttons.append(b)
            await update.message.reply_text(f"Which indicator on {text.upper()} do you want to remove condition",
                    reply_markup=ReplyKeyboardMarkup(buttons,  one_time_keyboard=True, resize_keyboard=True))
            return REMOVE_INDICATOR

    async def remove_indicator(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        text = update.message.text.strip().upper()
        if text not in context.user_data['list_indi']:
            buttons = []
            b = []
            i = 0
            for indi in context.user_data['list_indi']:
                b.append(indi)
                if len(b) == 3:
                    buttons.append(b)
                    b = []
            if len(b) != 0:
                buttons.append(b)
            await update.message.reply_text(f"Hmm, Seems like {text.upper()} do not have condition on {text}. Try using buttons below", 
                    reply_markup=ReplyKeyboardMarkup(buttons,  one_time_keyboard=True, resize_keyboard=True))
            return REMOVE_INDICATOR
        context.user_data['tech_indi'] = text
        select_query = "SELECT distinct direction FROM stockalert WHERE chat_id = %s and ticker = %s and indicator = %s"
        self.cursor.execute(select_query, (str(update.effective_chat.id), context.user_data['symbol'], text))
        rows = self.cursor.fetchall()
        context.user_data['list_direction'] = []
        buttons = []
        b = []
        i = 0
        for row in rows:
            b.append(configs.DIRECTION_BUTTON[0][row[0]])
            if len(b) == 3:
                buttons.append(b)
                b = []
            context.user_data['list_direction'].append(configs.DIRECTION_BUTTON[0][row[0]])
        if len(b) != 0:
                buttons.append(b)
        await update.message.reply_text(f"Which direction on {text} of {context.user_data['symbol']} do you want to remove condition", 
                reply_markup=ReplyKeyboardMarkup(buttons,  one_time_keyboard=True, resize_keyboard=True))
        return EXEC_REMOVE_COMMAND
    
    async def exec_remove_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        text = update.message.text.strip().lower()
        if text not in context.user_data['list_direction']:
            buttons = []
            b = []
            i = 0   
            for direction in context.user_data['list_direction']:
                b.append(direction)
                if len(b) == 3:
                    buttons.append(b)
                    b = []
            if len(b) != 0:
                buttons.append(b)
            await update.message.reply_text(f"Hmm, Seems like {text.upper()} is invalid or these is no condition. Try using buttons below", 
                    reply_markup=ReplyKeyboardMarkup(buttons,  one_time_keyboard=True, resize_keyboard=True))
            return EXEC_REMOVE_COMMAND
        else:
            ticker = context.user_data['symbol']
            indicator = context.user_data['tech_indi']
            direction = 0 if text == "less than" else 1
            delete_query = f"DELETE FROM stockalert WHERE chat_id = {str(update.effective_chat.id)} AND ticker = '{ticker}' and indicator = '{indicator}' and direction = {direction}"
            self.cursor.execute(delete_query)
            self.connection.commit()
            message = "Alert removed successfully! Use /list to see all your alert"
            logging.info(f"User remove condition at chat id {str(update.effective_chat.id)}: Success -- Detail: {ticker} - {indicator} - {configs.DIRECTION_BUTTON[0][direction]}")
            if direction == 1:
                self.r.zrem(f"{indicator}:{ticker}:gt", update.effective_chat.id)
            else:
                self.r.zrem(f"{indicator}:{ticker}:lt", update.effective_chat.id)
            await context.bot.send_message(chat_id=update.effective_chat.id, text=message)
            return END_CONVERSATION
# -------------------------------------- end of remove conversation --------------------------------------

    async def cancel(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        logging.info(f"Stop receiving alert from chat: {chat_id}")
        select_query = f"SELECT * FROM user WHERE chat_id = {str(chat_id)}"
        self.cursor.execute(select_query)
        row = self.cursor.fetchone()
        if row is not None:
            delete_condition_query = f"DELETE FROM user_alert_condition WHERE chat_id = {str(chat_id)}"
            self.cursor.execute(delete_condition_query)
            self.connection.commit()
            logging.info("Remove user info from db successfully")
        message = "Bye have a good time"
        await context.bot.send_message(chat_id=chat_id, text=message)

    async def command_unknown(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


if __name__ == '__main__':
    bot = Bot()
    bot.application.run_polling(timeout=6000)      



