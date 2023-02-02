import mysql.connector
from mysql.connector import Error
import configs
import logging
from telegram import KeyboardButton, ReplyKeyboardMarkup, Update
from telegram.ext import *
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

        # add_conv_handler = ConversationHandler(
        #     entry_points=[CommandHandler("add", self.add_condition)],
        #     states={
        #         ADD_SYMBOL: [MessageHandler(filters.TEXT & ~filters.COMMAND, self.add_symbol),],
        #         ADD_DIRECTION:[MessageHandler(filters.TEXT & ~filters.COMMAND, self.add_direction),],
        #         ADD_THRESHOLD: [MessageHandler(filters.TEXT & ~filters.COMMAND, self.add_threshold),],
        #         EXEC_ADD_COMMAND: [MessageHandler(filters.TEXT & ~filters.COMMAND, self.exec_add_command),]
        #     },
        #     fallbacks=[CommandHandler("add", self.add_condition), CommandHandler("remove", self.remove_condition)]
        # )

        self.application = ApplicationBuilder().token(configs.TOKEN)\
                                                .read_timeout(30)\
                                                .write_timeout(30)\
                                                .build()
        # self.application.add_handler(add_conv_handler, 1)
        self.application.add_handler(CommandHandler('start', self.start), 0)
        self.application.add_handler(CommandHandler('help', self.help), 0)
        # self.application.add_handler(CommandHandler('list', self.list_condition), 0)
        # self.application.add_handler(CommandHandler('cancel', self.cancel), 0)
        # self.application.add_handler(MessageHandler(filters.COMMAND & ~filters.Regex('^(\/add|\/start|\/list|\/remove|\/cancel|\/help|\/update|\/viewdata|\/predictdata)$'), self.command_unknown))

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
        logging.info(f"Start command at chat: {chat_id}")
        await context.bot.send_message(chat_id=chat_id, text=configs.WELCOME_MESSAGE)

    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat_id = update.effective_chat.id
        logging.info(f"Help command at chat: {chat_id}")
        await context.bot.send_message(chat_id=chat_id, text=configs.HELP_MESSAGE)


    # async def list_condition(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    #     chat_id = update.effective_chat.id
    #     logging.info(f"List condition command at chat: {chat_id}")
    #     select_query = "SELECT * FROM configs WHERE chat_id = %s"
    #     self.cursor.execute(select_query, (chat_id,))
    #     rows = self.cursor.fetchall()
        
    #     if rows is None or len(rows) == 0: 
    #         message = configs.NO_CONDITION_MESSAGE
    #         logging.info(f"List condition at chat id {chat_id}: Did not find any condition")
    #     else:
    #         message = "Your alert condition: \n"
    #         for row in rows:
    #             (chat_id, ticker, indicator, threshold, direction) = row
    #             message = message + "\nTicker " + ticker.upper()
    #             if direction == 0: 
    #                 message = message + f" has lower boundary on {indicator}: " + str(threshold)
    #             if direction == 1: 
    #                 message = message +  f" has upper boundary: {indicator}: " + str(threshold)
    #     await context.bot.send_message(chat_id=chat_id, text=message)
    #     logging.info(f"List condition at chat id {chat_id}: Success")

if __name__ == '__main__':
    bot = Bot()
    bot.application.run_polling()       



