import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("stocks.csv")
#convert into Datetime format
df['Date'] = pd.to_datetime(df['Date'])
#categorise by unique companies
Tickers = df['Ticker'].unique()
columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']

for col in columns:
    plt.figure(figsize=(12, 6))
    for ticker in Tickers:
        company_data = df[df['Ticker'] == ticker]
        plt.plot(company_data['Date'], company_data[col], label=ticker)
    #titles
    if col == 'Adj Close':
        title = "Adjusted Close Over Time"
        ylabel = "Adjusted Close"
    elif col == 'Volume':
        title = "Volume Traded Over Time"
        ylabel = "Volume"
    else:
        title = f"{col.title()} Prices Over Time"
        ylabel = col.title()

    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
