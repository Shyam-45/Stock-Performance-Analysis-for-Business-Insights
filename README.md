Stock Market Data Analysis and Trend Identification

- This project analyzes historical stock price data of a major Indian company using Python libraries. It involves data visualization, statistical analysis, and trend identification to generate actionable insights.


Features

1. Data Loading and Cleaning:
Imported data using Pandas and handled missing values.
Displayed basic information and performed exploratory data analysis.

2. Data Visualization:

Visualized closing prices over time using Matplotlib.
Created candlestick charts using mplfinance for detailed stock movement visualization.

3. Statistical Analysis:

Calculated daily return percentages using the formula: ((Close - Open) / Open) * 100.
Computed key statistics like average, median, and standard deviation of returns.

4. Moving Averages:

Calculated and plotted 50-day and 200-day moving averages for trend analysis.

5. Volatility Analysis:

Analyzed stock volatility using a rolling 30-day standard deviation.

6. Trend Identification:

Determined bullish and bearish market trends based on moving averages (50-day vs 200-day).


Tools and Libraries Used

Pandas: Data loading, cleaning, manipulation, and analysis.
NumPy: Efficient numerical computations.
Matplotlib: Visualization of time series data and charts.
mplfinance: Candlestick chart generation for stock price analysis.


How to Run ?

1. Install required libraries using the following command:
2. pip install pandas numpy matplotlib mplfinance
3. Place the dataset (infy_stock.csv) in the project directory.
4. Run the Python script: python stock_analysis.py


Results and Insights

1. Visualized stock performance and volatility.
2. Identified key market trends.
3. Gained actionable insights from statistical analysis.
