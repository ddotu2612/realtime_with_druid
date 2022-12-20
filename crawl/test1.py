import pandas as pd
import os
from datetime import datetime, timedelta, date
import random


codes = []
for name in os.listdir('data-all'):
    code = name.split('.')[0]
    codes.append(code)
print(codes)

from_date = date(2022,12,14)
to_date = date(2023,1,31)
dates = pd.date_range(from_date, to_date - timedelta(days=1),freq='d').tolist() #.values.tolist()
dates = [(date.strftime('%d/%m/%Y')) for date in dates]
print(dates)

# print(datetime.strptime(from_date, '%d/%m/%Y') + timedelta(days=1))
list_df = []

def gen_data(day, code):
    print(day + " - " + code)
    df = pd.DataFrame(columns=["ticker", "time", "close", "open", "high", "low", "volume"])

    len_cur = len(list_df)
    df_last = list_df[len_cur-1] if len_cur > 0 else 100
    close_last = df_last['close'][0] if len_cur > 0 else df_last

    max = close_last * 1.07
    min = close_last * 0.93
    print(close_last, min, max)

    # day
    ticker = code
    time = day
    open = round(random.uniform(min, max), 2)
    # random low price
    while 1:
        x = round(random.uniform(min, max), 2)
        if x <= open:
            break
    low = x
    # random high price
    while 1:
        y = round(random.uniform(min, max), 2)
        if y >= open:
            break
    high = y
    # random close price
    while 1:
        z = round(random.uniform(min, max), 2)
        if z >= low and z <= high:
            break
    close = z
    print(ticker, time, close, open, high, low, ' HIHI')

    df = pd.concat([df, pd.DataFrame.from_records([{
        "ticker": ticker,
        "time": time,
        "close": close,
        "open": open,
        "high": high,
        "low": low,
        "volume": round(random.uniform(1000, 500000000), 2)
    }])])

    return df

for code in codes:
    for date in dates:
        df = gen_data(date, code)
        list_df.append(df)

new_df = pd.concat(list_df,ignore_index=True)
new_df.to_csv('stock_fake.csv', index=False)

