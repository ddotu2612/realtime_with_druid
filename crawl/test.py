import pandas as pd
import os

# df_s = pd.DataFrame(columns=["ticker", "time", "close", "open", "high", "low", "colume"])
pd_list = []
for name in os.listdir('data-all'):
    file = os.path.join('data-all', name)
    df = pd.read_csv(file, header=None)
    pd_list.append(df)
new_df = pd.concat(pd_list,ignore_index=True)
new_df.to_csv('stock.csv', index=False)