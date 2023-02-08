from pydruid.client import *
import pandas as pd
from pydruid.db import connect
import redis


# def exec_to_df(druid_query):
#     conn = connect(host='localhost', port=8082, path='/druid/v2/sql/', scheme='http')
#     curs = conn.cursor()

    

#     df = pd.DataFrame(curs.execute(druid_query))

#     return df


# druid_query = """select * from datastock where TradingDate = '2023-01-27'"""
# df = exec_to_df(druid_query)

# res = df[["ticker", "Close", "Volume"]].values

# print(df)

# print(res)

# for i in res:
#     ticker, close, volume = i
#     print(ticker, close, volume)
#     if ticker == "AAA":
#         break


# r = redis.Redis()

# print(r.zrangebyscore(f"alert:PRICE:ABC:gt", 0, 7000))

