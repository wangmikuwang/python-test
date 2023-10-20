import tushare as ts
ts.set_token('7cbf4beb72d223898ffafdb826d7cb0879a3f372689e214461274361')
pro = ts.pro_api()
stock_code = '600000.SH'
start_date = '20230101'
end_date = '20231010'
df = pro.daily(ts_code=stock_code, start_date=start_date, end_date=end_date)
df['Profit'] = (df['close'] - df['open']) * 1000
print(df[['trade_date', 'open', 'close', 'Profit']])
