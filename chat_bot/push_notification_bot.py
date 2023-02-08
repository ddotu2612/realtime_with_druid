from concurrent.futures import thread
import logging
import configs
import telegram
from telegram.ext import *
import mysql.connector
from mysql.connector import Error
from kafka import KafkaConsumer
import redis
import threading
import json
import asyncio
from datetime import datetime, time

# read data from druid
from pydruid.client import *
import pandas as pd
from pydruid.db import connect

# import read_data_druid


class PushNotificationBot():
    def __init__(self, consumer_configs=None) -> None:
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
                logging.info(connection.get_server_info())
                self.cursor = connection.cursor()
                self.cursor.execute("select database();")
                record = self.cursor.fetchone()
                logging.info(f"You're connected to database: {record}")

        except Error as e:
            logging.error("Error while connecting to MySQL:\n" + e)

        self.r = redis.Redis()
        self.curs = connect(host='localhost', port=8082, path='/druid/v2/sql/', scheme='http').cursor()
        self.bot = telegram.Bot(token=configs.TOKEN)


    async def consume(self):
        query_stock_sql = """select * from datastock where TradingDate = '2023-01-27'"""
        df = pd.DataFrame(self.curs.execute(query_stock_sql))
        res_close = df[["ticker", "Close"]].values
        res_volume = df[["ticker", "Close"]].values
        print(res_close)                
        await self.process_messages(res_close, "PRICE")

    async def process_messages(self, messages, topic):
        print(len(messages))
        for message in messages:
            ticker, cur = message
            print(ticker, cur)
            # prev = self.r.get(f"{topic}:{ticker}")

            # if prev is None:
            #     self.r.set(f"{topic}:{ticker}", cur)
            #     return

            # if ticker == 'ACB' and topic == 'price':
            #     print(cur)

            # prev = float(prev)
            alert_chat_ids_lt = self.r.zrangebyscore(f"alert:{topic.upper()}:{ticker}:lt", cur, '+inf')
            print(alert_chat_ids_lt)
            if len(alert_chat_ids_lt) > 0:
                await self.send_alerts(alert_chat_ids_lt, ticker, topic, cur, 0)
            alert_chat_ids_gt = self.r.zrangebyscore(f"alert:{topic.upper()}:{ticker}:gt", 0, cur)
            print(alert_chat_ids_gt)
            if len(alert_chat_ids_gt) > 0:
                await self.send_alerts(alert_chat_ids_gt, ticker, cur, topic, 1)
            if ticker == 'ABC':
                break
            # self.r.set(f"{topic}:{ticker}", cur)


    async def send_alerts(self, chat_ids, ticker, cur_value, indicator, direction):
        if direction == 0:
            msg = configs.LT_MESSAGE
        else:
            msg = configs.GT_MESSAGE
        print(chat_ids)
        for chat_id in chat_ids:
            text_msg = msg.format(ticker, indicator, cur_value)
            print(text_msg)
            print(type(chat_id), chat_id)
            await self.bot.send_message(chat_id=chat_id.decode('utf-8'), text=text_msg)

    def __del__(self):
        self.r.quit()

if __name__ == "__main__":
    bot = PushNotificationBot()
    asyncio.run(bot.consume())