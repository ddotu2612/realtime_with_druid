from datetime import datetime
import random
import json
from kafka import KafkaProducer
import time
import pandas as pd
import numpy as np
from vnstock import *
from dotenv import load_dotenv
import os

load_dotenv()
KAFKA_BOOTSTRAP_SERVER = os.getenv('KAFKA_BOOTSTRAP_SERVER')
# KAFKA_HOST_IP=   
TOPIC = 'datastock'
kafka_servers = [KAFKA_BOOTSTRAP_SERVER]

# Messages will be serialized as JSON 
def serializer(message):
    return json.dumps(message).encode('utf-8')

kafka_p = KafkaProducer(
    # bootstrap_servers = [f'{KAFKA_HOST_IP}:9094'], 
    bootstrap_servers = kafka_servers, # connect kafka in k8s   
    value_serializer=serializer
)

# # crawler historical data in current day
def crawler():
    # list ticker
    codes = listing_companies()['ticker'].tolist()
    print(len(codes)) # 1631 ticker
   
    # get historical stock data from start_date to end_date
    now = datetime.now()
    yes = datetime.now() - timedelta(days=1)
    now_str = now.strftime("%Y-%m-%d")
    yes_str = yes.strftime("%Y-%m-%d")
    start_date =  yes_str
    end_date = now_str

    print(f"Start crawl data in date {now_str}")
    list_df = []
    for code in codes:
        
        try:
            df = stock_historical_data(symbol=code, start_date=start_date, end_date=end_date)
        except:
            continue

        df['ticker'] = code
        cols = df.columns.tolist()
        cols = cols[-1:] + cols[-2:-1] + cols[:-2]
        df = df[cols]
        list_df.append(df)
#         print('done ticker ', code)
        print(code)
    
    df_all = pd.concat(list_df, ignore_index=True)
#     df_all.to_csv('stock_crawl_new_full.csv', index=False)

    return df_all

# crawler()

# # create message to send to Kafka
def generate_message():
    df = crawler() # dataframe store historical data in current day
    # df = pd.read_csv(r'D:\DE\realtime_with_druid\crawl\stock_crawl_new_full.csv')
    df.columns = ['ticker', 'time', 'open', 'high', 'low', 'close', 'volume']
    # df['timestamp'] = pd.to_datetime(df['TradingDate'],format= '%Y-%m-%d').values.astype(np.int64) // 10 ** 9
    # df['date_convert'] = [datetime.fromtimestamp(x) for x in df['timestamp']]
    # lis = df.values.tolist()
    out = df.to_json(orient='records', lines=True).split('\n')
    # print(df)
    # print(out)
    return out

def send_messages_kafka():
    dummy_message = generate_message()
    print(type(dummy_message))
    for item in dummy_message[0:-1]:
        print(item)
        item = json.loads(item)
        # print(item)
        # Send it to our 'messages' topic
        print(f'Producing message @ {datetime.now()} | Message = {str(item)}')
        kafka_p.send(TOPIC, item)
        time.sleep(0.03)

# while True:
if __name__ == "__main__":
    send_messages_kafka()
    # time.sleep(60)