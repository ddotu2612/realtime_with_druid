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


class SendAlert():
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
                print(connection.get_server_info())
                self.cursor = connection.cursor()
                self.cursor.execute("select database();")
                record = self.cursor.fetchone()
                print(f"connected to database: {record}")

        except Error as e:
            print("Error while connecting to MySQL:\n" + e)

        self.r = redis.Redis()
        print("connected to redis")
        self.curs = connect(host='localhost', port=8082, path='/druid/v2/sql/', scheme='http').cursor()
        self.bot = telegram.Bot(token=configs.TOKEN)


    async def read_data(self):
        
        query_stock_sql = """select * from datastock where __time = TIMESTAMP '2023-02-28 00:00:00'"""
        df = pd.DataFrame(self.curs.execute(query_stock_sql))
        res_close = df[["ticker", "Close"]].values
        res_volume = df[["ticker", "Volume"]].values
        # print(res_close)
        # print(res_volume)
        while 1:
            await self.processMessages(res_close, "PRICE")
            await self.processMessages(res_volume, "VOLUME")
            await asyncio.sleep(10)

    async def processMessages(self, messages, topic):
        print(len(messages))
        for message in messages:
            ticker, cur = message
            # # if ticker == 'APF':
            # print (ticker, cur)
            alert_chat_ids_lt = self.r.zrangebyscore(f"{topic.upper()}:{ticker}:lt", cur, '+inf')
            
            if len(alert_chat_ids_lt) > 0:
                print(alert_chat_ids_lt)
                await self.send_alerts(alert_chat_ids_lt, ticker, cur, topic, 0)
            alert_chat_ids_gt = self.r.zrangebyscore(f"{topic.upper()}:{ticker}:gt", 0, cur)
            
            if len(alert_chat_ids_gt) > 0:
                print(alert_chat_ids_gt)
                await self.send_alerts(alert_chat_ids_gt, ticker, cur, topic, 1)
            # if ticker == 'ABC':
            #     break
            # self.r.set(f"{topic}:{ticker}", cur)


    async def send_alerts(self, chat_ids, ticker, cur_value, indicator, direction):
        # print(chat_ids, ticker, cur_value, indicator, direction)
        # print('haha')
        if direction == 0:
            msg = configs.LT_MESSAGE
        else:
            msg = configs.GT_MESSAGE
        print('chat_ids', chat_ids)
        if direction == 0:
            for chat_id in chat_ids:
                if chat_id.decode('utf-8') == '1': continue
                threshold = self.r.get(f"{indicator}:{ticker}:{chat_id.decode('utf-8')}:lt:cur")
                threshold = float(threshold)

                prev_lt = self.r.get(f"{indicator}:{ticker}:{chat_id.decode('utf-8')}:lt:prev")
                print(prev_lt)
                    
                if prev_lt is None:
                    self.r.set(f"{indicator}:{ticker}:{chat_id.decode('utf-8')}:lt:prev", threshold)
                    
                    percent = round(abs(threshold - cur_value) * 100 / threshold, 2)
                    text_msg = msg.format(ticker, indicator, percent, cur_value)
                    await self.bot.send_message(chat_id=chat_id.decode('utf-8'), text=text_msg)
                else:
                    prev_lt = float(prev_lt)
                    print("prev: ", prev_lt, " threshold: ", threshold)
                    if (prev_lt != threshold):
                        self.r.set(f"{indicator}:{ticker}:{chat_id.decode('utf-8')}:lt:prev", threshold)

                        percent = round(abs(threshold - cur_value) * 100 / threshold, 2)
                        text_msg = msg.format(ticker, indicator, percent, cur_value)
                        await self.bot.send_message(chat_id=chat_id.decode('utf-8'), text=text_msg)

        else:
            for chat_id in chat_ids:
                if chat_id.decode('utf-8') == '1': continue
                threshold = self.r.get(f"{indicator}:{ticker}:{chat_id.decode('utf-8')}:gt:cur")
                threshold = float(threshold)
                prev_gt = self.r.get(f"{indicator}:{ticker}:{chat_id.decode('utf-8')}:gt:prev")
                print(prev_gt)
                if prev_gt is None:
                    self.r.set(f"{indicator}:{ticker}:{chat_id.decode('utf-8')}:gt:prev", threshold)
                    percent = round(abs(threshold - cur_value) * 100 / threshold, 2)
                    text_msg = msg.format(ticker, indicator, percent, cur_value)
                    await self.bot.send_message(chat_id=chat_id.decode('utf-8'), text=text_msg)
                else:
                    prev_gt = float(prev_gt)
                    print("prev: ", prev_gt, " threshold: ", threshold)
                    if (prev_gt != threshold):
                        self.r.set(f"{indicator}:{ticker}:{chat_id.decode('utf-8')}:gt:prev", threshold)

                        percent = round(abs(threshold - cur_value) * 100 / threshold, 2)
                        text_msg = msg.format(ticker, indicator, percent, cur_value)
                        await self.bot.send_message(chat_id=chat_id.decode('utf-8'), text=text_msg)

    def __del__(self):
        self.r.quit()

if __name__ == '__main__':
    bot = SendAlert()
    loop = asyncio.get_event_loop()
    # loop.create_task(bot.read_data())
    loop.run_until_complete(bot.read_data())
        