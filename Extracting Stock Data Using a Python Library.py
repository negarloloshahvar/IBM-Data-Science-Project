import yfinance as yf
import pandas as pd

apple = yf.Ticker('AAPL')
apple_info = apple.info
apple_info['country']
apple_share_price_data = apple.history(period='max')
# print(apple_share_price_data.at[0,'Volume'])
# apple_share_price_data.reset_index(inplace= True)
# apple_share_price_data.plot(x= 'Date', y= 'Open')
#
# apple_dividends = apple.dividends
# apple.dividends.plot()