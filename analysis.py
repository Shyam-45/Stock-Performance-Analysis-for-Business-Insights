import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
# import matplotlib.dates as mdates
# import numpy as np

file_path = 'infy_stock.csv'
df = pd.read_csv(file_path) #loaded dataset

#displaying first 10 rows of dataset
print("First 10 rows of dataset:")
print(df.head(10))

# Check for missing values in the dataset
print("\nMissing values before handling:")
print(df.isnull().sum())


# Convert object dtype columns to their inferred types (numeric, datetime, etc.)
df = df.infer_objects(copy=False)

# Handle missing values using linear interpolation
df.interpolate(method='linear', inplace=True)

# Verify that missing values are handled
print("\nMissing values after handling:")
print(df.isnull().sum())


# Convert the Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Set the Date as the index
df.set_index('Date', inplace=True)

# Plot the closing price over time
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Close'], label='Closing Price', color='blue')
plt.title('Closing Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid()
plt.show()

# using mplfinance
# Plot a candlestick chart for the stock prices
mpf.plot(df, type='candle', volume=True, style='charles',
         title='Candlestick Chart for Stock Prices',
         ylabel='Price', ylabel_lower='Volume')

# Calculate daily return percentage
df['Daily Return (%)'] = ((df['Close'] - df['Open']) / df['Open']) * 100

# Calculate average of daily returns
average_return = df['Daily Return (%)'].mean()

# Calculate median of daily returns
median_return = df['Daily Return (%)'].median()

# Calculate standard deviation of closing prices
std_dev_close = df['Close'].std()

# Print the results
print(f"Average Daily Return: {average_return:.2f}%")
print(f"Median Daily Return: {median_return:.2f}%")
print(f"Standard Deviation of Closing Prices: {std_dev_close:.2f}")

# Calculate the 50-day and 200-day moving averages
df['50-day MA'] = df['Close'].rolling(window=50).mean()
df['200-day MA'] = df['Close'].rolling(window=200).mean()

# Plot the closing price and moving averages
plt.figure(figsize=(12, 6))
plt.plot(df['Close'], label='Closing Price', color='blue', alpha=0.5)
plt.plot(df['50-day MA'], label='50-day Moving Average', color='orange')
plt.plot(df['200-day MA'], label='200-day Moving Average', color='red')

# Adding titles and labels
plt.title('Closing Price and Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid()
plt.show()

# Calculate the 30-day rolling standard deviation (volatility)
df['30-day Volatility'] = df['Close'].rolling(window=30).std()

# Plot the volatility
plt.figure(figsize=(12, 6))
plt.plot(df['30-day Volatility'], label='30-day Volatility', color='purple')

# Adding titles and labels
plt.title('30-day Rolling Standard Deviation (Volatility) of Closing Prices')
plt.xlabel('Date')
plt.ylabel('Volatility')
plt.legend()
plt.grid()
plt.show()

# Identify bullish and bearish trends
df['Trend'] = 'Neutral'
df.loc[df['50-day MA'] > df['200-day MA'], 'Trend'] = 'Bullish'
df.loc[df['50-day MA'] < df['200-day MA'], 'Trend'] = 'Bearish'

# Plot the closing price and moving averages
plt.figure(figsize=(14, 7))
plt.plot(df['Close'], label='Closing Price', color='blue', alpha=0.5)
plt.plot(df['50-day MA'], label='50-day Moving Average', color='orange')
plt.plot(df['200-day MA'], label='200-day Moving Average', color='red')

# Mark bullish and bearish trends with shaded areas
for i in range(1, len(df)):
    if df['Trend'].iloc[i] == 'Bullish' and df['Trend'].iloc[i - 1] == 'Bearish':
        plt.axvspan(df.index[i - 1], df.index[i], color='green', alpha=0.3, label='Bullish Trend' if 'Bullish Trend' not in plt.gca().get_legend_handles_labels()[1] else "")
    elif df['Trend'].iloc[i] == 'Bearish' and df['Trend'].iloc[i - 1] == 'Bullish':
        plt.axvspan(df.index[i - 1], df.index[i], color='red', alpha=0.3, label='Bearish Trend' if 'Bearish Trend' not in plt.gca().get_legend_handles_labels()[1] else "")

# Adding titles and labels
plt.title('Stock Price with Moving Averages and Trend Areas')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid()
plt.show()


# ********************************************************************************************

# without using mplfinance

# Function to create a candlestick chart
# def plot_candlestick(data):
#     fig, ax = plt.subplots(figsize=(12, 6))

#     for i in range(len(data)):
#         # Extract data for the current day
#         open_price = data['Open'].iloc[i]
#         close_price = data['Close'].iloc[i]
#         high_price = data['High'].iloc[i]
#         low_price = data['Low'].iloc[i]
#         date = data.index[i]

#         # Determine the color of the candlestick
#         if close_price >= open_price:
#             color = 'green'  # Bullish
#             lower = open_price
#             height = close_price - open_price
#         else:
#             color = 'red'    # Bearish
#             lower = close_price
#             height = open_price - close_price

#         # Draw the candle
#         ax.add_patch(plt.Rectangle((mdates.date2num(date) - 0.2, lower), 0.4, height, color=color))
        
#         # Draw the high and low lines
#         ax.plot([mdates.date2num(date), mdates.date2num(date)], [low_price, high_price], color='black')

#     # Formatting the x-axis
#     ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
#     ax.xaxis.set_major_locator(mdates.DayLocator(interval=5))
#     plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')

#     ax.set_title('Candlestick Chart for Stock Prices')
#     ax.set_ylabel('Price')
#     plt.grid()
#     plt.show()

# # Call the function to plot the candlestick chart
# plot_candlestick(df)

# **************************************************************************************