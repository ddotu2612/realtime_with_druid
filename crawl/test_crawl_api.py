from vnstock import *

['24H', 'AAA', 'AAM']

try:
    df =  stock_historical_data(symbol='AAA', 
                            start_date="2021-01-01", 
                            end_date='2022-02-25')
    df['ticker'] = 'AAA'
    cols = df.columns.tolist()
    cols = cols[-1:] + cols[-2:-1] + cols[:-2]
    df = df[cols]
    
except:
    print("haha")

print(df.head())

# list_code = pd.read_excel("code_stock.xlxs")
# codes = list_code[(list_code["Unnamed: 0"].str.len() == 3)]["Unnamed: 0"].tolist()
# print(len(codes))
# list_df = []
# i = 0
# for code in codes[0:1000]:
#     start_date = '2022-11-01'
#     end_date = '2022-12-13'
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
# new_df.to_csv('stock_crawl_new.csv', index=False)