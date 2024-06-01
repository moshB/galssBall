
import yfinance as yf
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np  # For generating sine wave
avar=150
days=30
ticker = yf.Ticker("NVDA")

# Today's date
today = pd.Timestamp.today()

# Set the start date 150 days ago
start_date = today - pd.Timedelta(days=avar+days)

# Download data (includes adjusted closing price)
data = ticker.history(start=start_date, end=today, interval="1d")
avarge=[]
for i in range(days):
    end=len(data["Close"])-i
    start = end-avar
    average_price = data["Close"][start:end].mean()
    avarge.append(average_price)
price=[]
for i in range(days):
    end=len(data["Close"])-i
    start = end-1
    average_price = data["Close"][start:end].mean()
    price.append(average_price)

price.reverse()
avarge.reverse()

x = range(days)  # Adjust the range as needed

# Calculate y values for both functions

# Create the plot
plt.plot(x, price, label="price")  # Label for x^2 curve
plt.plot(x, avarge, label="avarge")  # Label for sin curve

# Add labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Plot of y = x^2 and y = sin(x)")

# Add legend
plt.legend()  # Show labels for each curve

# Show the plot
plt.show()






