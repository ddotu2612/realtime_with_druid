from vnstock import *
import pandas as pd
import numpy as np

# print(listing_companies())
x = listing_companies()['ticker'].tolist()
x.sort()

for i, item in enumerate(x):
    if (i + 1) % 10:
        print(f'{item}, ', end='')
    else:
        print(f'{item}, \n')
# ['24H', 'AAA', 'AAM']

# try:
#     now = datetime.now()
#     yes = datetime.now() - timedelta(days=1)
#     now_str = now.strftime("%Y-%m-%d")
#     yes_str = yes.strftime("%Y-%m-%d")

#     start_date =  yes_str
#     end_date = now_str

#     df =  stock_historical_data(symbol='YTC', 
#                             start_date=start_date, 
#                             end_date=end_date)
#     df['ticker'] = 'YTC'
#     cols = df.columns.tolist()
#     cols = cols[-1:] + cols[-2:-1] + cols[:-2]
#     df = df[cols]
#     print(df.head())
# except:
#     now = datetime.now()
#     yes = datetime.now() - timedelta(days=1)
#     now_str = now.strftime("%Y-%m-%d")
#     yes_str = yes.strftime("%Y-%m-%d")

#     start_date =  yes_str
#     end_date = now_str
#     print(yes_str, now_str)



# list_code = pd.read_excel("code_stock.xlxs")
# codes = listing_companies()['ticker'].tolist()
# print(len(codes))
# list_df = []
# i = 0
# for code in codes:
#     start_date = '2022-01-01'
#     end_date = '2023-01-27'
#     try:
#         df =  stock_historical_data(symbol=code, start_date=start_date, end_date=end_date)
#     except:
#         continue
#     df['ticker'] = code
#     cols = df.columns.tolist()
#     cols = cols[-1:] + cols[-2:-1] + cols[:-2]
#     df = df[cols]
#     list_df.append(df)
#     i = i + 1
#     print('done ma: ', code, " ", i)

# new_df = pd.concat(list_df,ignore_index=True)
# new_df.to_csv('stock_crawl_new_full.csv', index=False)