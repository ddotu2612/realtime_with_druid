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

def gen_data(day, code):
    print(day + " - " + code)
    df = pd.DataFrame(columns=["ticker", "time", "close", "open", "high", "low", "volume"])
    df = pd.concat([df, pd.DataFrame.from_records([{
        "ticker": code,
        "time": day,
        "close": random.randint(50, 1440),
        "open": random.randint(50, 1440),
        "high": random.randint(50, 1440),
        "low": random.randint(50, 1440),
        "volume": random.randint(1000, 500000000)
    }])])

    return df
list_df = []
for code in codes:
    for date in dates:
        df = gen_data(date, code)
        list_df.append(df)

new_df = pd.concat(list_df,ignore_index=True)
new_df.to_csv('stock_fake.csv', index=False)

