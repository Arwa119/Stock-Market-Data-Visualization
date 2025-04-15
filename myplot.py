import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("stocks.csv")
df['Date'] = pd.to_datetime(df['Date'])

#creation of main folder and subfolders for different plot types
mainFolder = "matplotlib_outputs"
plotTypes = ["line_plots", "bar_plots", "pie_charts", "area_plots", "scatter_plots", "histograms", "box_plots"]
folders = {}
for type in plotTypes:
    folderPath = os.path.join(mainFolder, type)
    os.makedirs(folderPath, exist_ok=True)
    folders[type] = folderPath

Tickers = df['Ticker'].unique()

#Line Plots for intercompany comparison
columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
for col in columns:
    plt.figure(figsize=(12, 6))
    for ticker in Tickers:
        company = df[df['Ticker'] == ticker]
        plt.plot(company['Date'], company[col], label=ticker)
    title = f"{col} Over Time" if col not in ['Adj Close', 'Volume'] else (
        "Adjusted Close Over Time" if col == 'Adj Close' else "Volume Traded Over Time")
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel(col)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{folders['line_plots']}/{col}_LinePlot.png")
    plt.close()

#Bar Plot: Highest Closing Price per Company
highestClosing = df.groupby('Ticker')['Close'].max().reset_index()
plt.figure(figsize=(8, 6))
plt.bar(highestClosing['Ticker'], highestClosing['Close'], color='green')
plt.title('Highest Closing Price per Company')
plt.xlabel('Company')
plt.ylabel('Closing Price')
plt.savefig(f"{folders['bar_plots']}/Bar_Highest_Closing_Price.png")
plt.close()

#Pie Chart: Total Volume per Company
totalVolume = df.groupby('Ticker')['Volume'].sum()
plt.figure(figsize=(8, 6))
plt.pie(totalVolume, labels=totalVolume.index, autopct='%1.1f%%', startangle=140)
plt.title('Share of Total Volume per Company')
plt.savefig(f"{folders['pie_charts']}/Pie_Total_Volume.png")
plt.close()

#Area Plot: Cumulative Close Price 
cumulativeClose = df.groupby(['Date', 'Ticker'])['Close'].sum().unstack()
cumulativeClose.fillna(0, inplace=True)
cumulativeClose = cumulativeClose.cumsum()
plt.figure(figsize=(12, 6))
cumulativeClose.plot.area(ax=plt.gca())
plt.title('Cumulative Close Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Cumulative Close')
plt.savefig(f"{folders['area_plots']}/Area_Cumulative_Close.png")
plt.close()

#scatter: Open vs Close for Each Company
for ticker in Tickers:
    cmp_df = df[df['Ticker'] == ticker]
    plt.figure(figsize=(8, 6))
    plt.scatter(cmp_df['Open'], cmp_df['Close'], alpha=0.7)
    plt.title(f"Open vs Close Price: {ticker}")
    plt.xlabel("Open Price")
    plt.ylabel("Close Price")
    plt.savefig(f"{folders['scatter_plots']}/Scatter_{ticker}_OpenVsClose.png")
    plt.close()

#Histogram: Distribution of Volume
plt.figure(figsize=(10, 6))
for ticker in Tickers:
    cmp_df = df[df['Ticker'] == ticker]
    plt.hist(cmp_df['Volume'], bins=20, alpha=0.5, label=ticker)
plt.title("Volume Distribution per Company")
plt.xlabel("Volume")
plt.ylabel("Frequency")
plt.legend()
plt.savefig(f"{folders['histograms']}/Histogram_Volume_Distribution.png")
plt.close()

#Box Plots
for col in ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']:
    plt.figure(figsize=(10, 6))
    data_by_company = [df[df['Ticker'] == ticker][col] for ticker in Tickers]
    plt.boxplot(data_by_company, tick_labels=Tickers)
    plt.title(f"Distribution of {col} by Company")
    plt.xlabel("Company")
    plt.ylabel(col)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{folders['box_plots']}/BoxPlot_{col}.png")
    plt.close()

