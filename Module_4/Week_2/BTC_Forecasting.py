import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates 
from mplfinance.original_flavor import candlestick_ohlc
import datetime

df = pd.read_csv('....\AIO_2024_Exercise\Module_4\Week_2\Data\BTC-Daily.csv')
df = df.drop_duplicates()

# Range of dates coverred
df['date'] = pd.to_datetime(df['date'])
date_range = str(df['date'].dt.date.min()) + " to " + str(df['date'].dt.date.max())
print(date_range)

# add column day, month, year
df['day'] = df['date'].dt.day
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year
unique_years = pd.unique(df['year'])

for year in unique_years:

    dates = pd.date_range(start = f"{year}-01-01", end = f'{year}-12-31', freq = 'D')
    year_month_day = pd.DataFrame({'date': dates})
    year_month_day['year'] = year_month_day['date'].dt.year
    year_month_day['month'] = year_month_day['date'].dt.month
    year_month_day['day'] = year_month_day['date'].dt.day

    merger_data = pd.merge(year_month_day, df, on = ['year', 'month', 'day'], how = 'left')
    # Plot
    plt.figure(figsize = (10, 6))
    plt.plot(merger_data['date_x'], merger_data['close'])
    plt.title(f'Bitcoin Closing Prices - {year}')
    plt.xlabel('Date')
    plt.ylabel('Closing Price (USD)')
    plt.xticks(rotation = 45)
    plt.tight_layout()
    plt.show()
###############################
# candlestick chart 2019-2022
###############################

# Filter data for 2019 2022
df_filtered = df[(df['date'] >= '2019-01-01') & (df['date'] <= '2022-12-31')]

# Convert date to matplotlib format
df_filtered['date'] = df_filtered['date'].map(mdates.date2num)

# Create the candlestick chart
fig, ax = plt.subplots(figsize = (20, 6))

candlestick_ohlc(ax, df_filtered[['date', 'open', 'high', 'low', 'close']].values, width = 0.6, colorup = 'g', colordown = 'r')

ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
fig.autofmt_xdate()

plt.title('Bitcoin Candlestick chart 2019 - 2022')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.grid(True)
plt.show()