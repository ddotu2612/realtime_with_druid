from datetime import datetime
import random
import json
from kafka import KafkaProducer
import time
import pandas as pd
import numpy as np

from vnstock import *

KAFKA_HOST_IP="localhost"
TOPIC = 'datastock'

# Messages will be serialized as JSON 
def serializer(message):
    return json.dumps(message).encode('utf-8')

kafka_p = KafkaProducer(
    bootstrap_servers = [f'{KAFKA_HOST_IP}:9094'],  
    value_serializer=serializer
)

# crawler historical data in current day
def crawler():
    # list ticker
    codes = listing_companies()['ticker'].tolist()
    print(len(codes)) # 1631 ticker

    list_df = []
    for code in codes:
        # get historical stock data from start_date to end_date
        now = datetime.now()
        yes = datetime.now() - timedelta(days=1)
        now_str = now.strftime("%Y-%m-%d")
        yes_str = yes.strftime("%Y-%m-%d")

        start_date =  yes_str
        end_date = now_str
        try:
            df = stock_historical_data(symbol=code, start_date=start_date, end_date=end_date)
        except:
            continue

        df['ticker'] = code
        cols = df.columns.tolist()
        cols = cols[-1:] + cols[-2:-1] + cols[:-2]
        df = df[cols]
        list_df.append(df)
        print('done ticker ', code)
    
    df_all = pd.concat(list_df, ignore_index=True)

    return df_all

# create message to send to Kafka
def generate_message():
    df = crawler() # dataframe store historical data in current day

    df['timestamp'] = pd.to_datetime(df['TradingDate'],format= '%Y-%m-%d').values.astype(np.int64) // 10 ** 9
    # df['date_convert'] = [datetime.fromtimestamp(x) for x in df['timestamp']]
    # lis = df.values.tolist()
    out = df.to_json(orient='records', lines=True).split('\n')
    # print(df)
    # print(out)
    return out

def send_messages_kafka():
    dummy_message = generate_message()
    print(type(dummy_message))
    for item in dummy_message:
        item = json.loads(item)
        # print(item)
        # Send it to our 'messages' topic
        print(f'Producing message @ {datetime.now()} | Message = {str(item)}')
        kafka_p.send(TOPIC, item)

# while True:
send_messages_kafka()
    # time.sleep(60)