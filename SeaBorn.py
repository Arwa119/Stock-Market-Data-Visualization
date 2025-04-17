import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
import os

# inter company comaparison


main_folder = "data"
if not os.path.exists(main_folder):
     os.makedirs(main_folder)

inter_company = os.path.join(main_folder,'inter_company')
if not os.path.exists(inter_company):
        os.makedirs(inter_company)

df = pd.read_csv('stocks.csv')
print("Missing values before cleaning:")
print(df.isnull().sum())
df['Date'] = pd.to_datetime(df['Date'])
numeric_columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
for column in numeric_columns:
    column_mean = df[column].mean()
    df[column] = df[column].fillna(column_mean)


df['Ticker'] = df['Ticker'].fillna('Unknown')
df = df.dropna()
# print("Missing values after cleaning:")
# print(df.isnull().sum())
# print(f"Total rows after cleaning: {len(df)}")

# ---- open prices of companies over time ----

plt.figure(figsize=(12,6))
sns.set_style("whitegrid")
sns.lineplot( data = df , x='Date', y ='Open' , hue='Ticker',marker='o')
plt.xlabel('Date',fontsize=12,fontweight='bold')
plt.ylabel('Opening Prices(USD)',fontsize=12,fontweight='bold')
plt.title('Opening Prices Over Time', fontsize=16, fontweight='bold')
plt.legend(title='Company' ,loc="upper right")
plt.savefig(f"{inter_company}/OpeningPrices_of_Companies.png")
plt.close()



# ---- closing prices of comapnies over time ----

plt.figure(figsize=(12,6))
sns.set_style("whitegrid")
sns.lineplot(data=df,x='Date',y='Close', hue='Ticker',marker='o')
plt.legend(title='Company' ,loc="upper right")
plt.title('Closing Prices Over Time', fontsize=16,fontweight='bold')
plt.xlabel('Date',fontsize=12,fontweight='bold')
plt.ylabel('Closing Prices(USD)',fontsize=12,fontweight='bold')
plt.savefig(f"{inter_company}/Closing_Prices.png")
plt.close()


# ---- Highest Prices Over Time ----

plt.figure(figsize=(12,6))
sns.set_style("whitegrid")
sns.lineplot(data=df,x='Date',y='High', hue='Ticker',marker='o')
plt.legend(title='Company' ,loc="upper right")
plt.title('Highest Price Per Day', fontsize=16,fontweight='bold')
plt.xlabel('Date',fontsize=12,fontweight='bold')
plt.ylabel('Highest Price(USD)',fontsize=12,fontweight='bold')
plt.savefig(f"{inter_company}/Highest_Prices.png")
plt.close()

# ---- Lowest Price Over Time ----

plt.figure(figsize=(12,6))
sns.set_style("whitegrid")
sns.lineplot(data=df,x='Date',y='Low', hue='Ticker',marker='o')
plt.legend(title='Company' ,loc="upper right")
plt.title('Lowest Price Per Day', fontsize=16,fontweight='bold')
plt.xlabel('Date',fontsize=12,fontweight='bold')
plt.ylabel('Lowest Price(USD)',fontsize=12,fontweight='bold')
plt.savefig(f"{inter_company}/Lowest_Prices.png")
plt.close()


# ---- Adj Close Over Time----

plt.figure(figsize=(12,6))
sns.lineplot(data=df, x='Date',y='Adj Close',hue='Ticker',marker='o')
sns.set_style('whitegrid')
plt.legend(title='Company',loc='upper right')
plt.title('Adjusted Clsoe Over Time', fontsize=16,fontweight='bold')
plt.xlabel('Date',fontsize=12,fontweight='bold')
plt.ylabel('Adjusted Close(USD)',fontsize=12,fontweight='bold')
plt.savefig(f"{inter_company}/Adj_Close.png")
plt.close()

# ---- Volume of stock sold ----

plt.figure(figsize=(12,6))
sns.lineplot(data=df, x='Date',y='Volume',hue='Ticker',marker='o')
sns.set_style('whitegrid')
plt.legend(title='Company',loc='upper right')
plt.title('Volume Of Shares Traded Per Company Per Day', fontsize=16,fontweight='bold')
plt.xlabel('Date', fontsize=12,fontweight='bold')
plt.ylabel('Volume', fontsize=12,fontweight='bold')
plt.savefig(f"{inter_company}/Volume.png")
plt.close()

# ---- Highest Closing Price per Company ----

max_close = df.groupby("Ticker")["Close"].max().reset_index()
max_close.rename(columns={"Close": "Max_Close"}, inplace=True)
sns.set_style("whitegrid")
plt.figure(figsize=(8, 5))
sns.barplot(data=max_close, x="Ticker", y="Max_Close")
plt.title("Highest Closing Price per Company", fontsize=14, fontweight='bold')
plt.xlabel("Company", fontsize=12)
plt.ylabel("Max Closing Price (USD)", fontsize=12)
plt.savefig(f"{inter_company}/Highest_Closing.png")
plt.close()

# ---- Daily Price Range (High - Low) Over Time ----

df['Daily_Range'] = df['High'] - df['Low']
sns.set_style("whitegrid")
plt.figure(figsize=(12, 6))
for company in df['Ticker'].unique():
    company_data = df[df['Ticker'] == company]
    sns.lineplot(data=company_data, x='Date', y='Daily_Range', label=company)
    plt.fill_between(company_data['Date'], company_data['Daily_Range'], alpha=0.2)
plt.title("Daily Price Range (High - Low) Over Time", fontsize=16, fontweight='bold')
plt.xlabel("Date", fontsize=12)
plt.ylabel("Price Range (USD)", fontsize=12)
plt.legend(title='Company')
plt.savefig(f"{inter_company}/Daily_Price_Range.png")
plt.close()

# ---- Total Trading Volume by Company ----

volume_by_company = df.groupby('Ticker')['Volume'].sum()
plt.figure(figsize=(6, 6))
plt.pie(volume_by_company, labels=volume_by_company.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title('Total Trading Volume by Company', fontsize=14, fontweight='bold')
plt.savefig(f"{inter_company}/Trading_Volume.png")
plt.close()

# ---- Distribution of Opening Prices ----

sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x="Open", bins=20, kde=True, color="skyblue")
plt.title("Distribution of Opening Prices", fontsize=16, fontweight='bold')
plt.xlabel("Opening Price (USD)", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.savefig(f"{inter_company}/Distribution_OpeningPrc.png")
plt.close()

# ---- Volume vs Adjusted Close Price ----

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="Volume", y="Adj Close", hue="Ticker", palette="deep", s=100)
plt.title("Volume vs Adjusted Close Price", fontsize=14, fontweight='bold')
plt.xlabel("Trading Volume", fontsize=12)
plt.ylabel("Adjusted Close Price (USD)", fontsize=12)
plt.savefig(f"{inter_company}/Vol_vs_AdjClose.png")
plt.close()

# -----COMPANY WISE DATA VISUALIZATION----

companies = df['Ticker'].unique()
for company in companies:
    df_cmp = df[df['Ticker']==company]
    
    company_folder = os.path.join(main_folder, company)
    if not os.path.exists(company_folder):
        os.makedirs(company_folder)

    plt.figure(figsize=(10,6))
    sns.lineplot(data=df_cmp,x='Date',y='Open',marker='o')
    plt.title(f"Open Prices of {company}",fontsize=16,fontweight='bold')
    plt.xlabel('Date',fontsize=12,fontweight='bold')
    plt.ylabel('Opening Prices',fontsize=12,fontweight='bold')
    plt.savefig(f"{company_folder}/{company}_OpenPrice.png")
    plt.close()

    plt.figure(figsize=(10,6))
    sns.lineplot(data=df_cmp,x='Date',y='Close',marker='o')
    plt.title(f"Closing Prices of {company}",fontsize=16,fontweight='bold')
    plt.xlabel('Date',fontsize=12,fontweight='bold')
    plt.ylabel('Closing Prices',fontsize=12,fontweight='bold')
    plt.savefig(f"{company_folder}/{company}_ClosePrice.png")
    plt.close()

    plt.figure(figsize=(10,6))
    sns.lineplot(data=df_cmp,x='Date',y='High',marker='o',color='Blue')
    sns.lineplot(data=df_cmp,x='Date',y='Low',marker='x',color='red')
    plt.title(f"High and  Low Prices of {company} Over Time",fontsize=16,fontweight='bold')
    plt.xlabel('Date',fontsize=12,fontweight='bold')
    plt.ylabel('Prices',fontsize=12,fontweight='bold')
    plt.savefig(f"{company_folder}/{company}_Prices.png")
    plt.close()

    plt.figure(figsize=(10,6))
    sns.lineplot(data=df_cmp,x='Date',y='Volume',color='purple')
    plt.title(f"Trading Volumn of {company} Over Time",fontsize=16,fontweight='bold')
    plt.xlabel('Date',fontsize=12,fontweight='bold')
    plt.ylabel('Volume',fontsize=12,fontweight='bold')
    plt.savefig(f"{company_folder}/{company}_Volume.png")
    plt.close()



# ---------- Matplotlib Implementation--------------

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

# --------- Pnadas Implementation ----------

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("stocks.csv")
df["Date"] = pd.to_datetime(df["Date"])

tickers = df["Ticker"].unique()

# Create a histogram using pandas plot
plt.figure(figsize=(10, 6))
for ticker in tickers:
    cmp_df = df[df["Ticker"] == ticker]
    cmp_df["Volume"].plot(kind="hist", bins=20, alpha=0.5, label=ticker)
plt.title("Volume Distribution per Company", fontsize=14, fontweight='bold')
plt.xlabel("Volume")
plt.ylabel("Frequency")
plt.legend()
plt.savefig("Histogram_Volume_Distribution_PandasOnly.png")
plt.close()


cumulative_close = df.groupby(['Date', 'Ticker'])['Close'].sum().unstack()
cumulative_close.fillna(0, inplace=True)
cumulative_close = cumulative_close.cumsum()

# Plot using pandas area plot
plt.figure(figsize=(12, 6))
cumulative_close.plot.area(ax=plt.gca(), alpha=0.6)
plt.title("Cumulative Close Prices Over Time", fontsize=14, fontweight='bold')
plt.xlabel("Date")
plt.ylabel("Cumulative Close Price (USD)")
plt.legend(title='Company')
plt.savefig("Area_Cumulative_Close_PandasOnly.png")
plt.close()

# Create a new column for Daily Price Range
df['Daily_Range'] = df['High'] - df['Low']

# Set up the figure
plt.figure(figsize=(12, 6))
for company in df['Ticker'].unique():
    company_data = df[df['Ticker'] == company]
    plt.plot(company_data['Date'], company_data['Daily_Range'], label=company)
    plt.fill_between(company_data['Date'], company_data['Daily_Range'], alpha=0.2)
plt.title("Daily Price Range (High - Low) Over Time", fontsize=16, fontweight='bold')
plt.xlabel("Date", fontsize=12)
plt.ylabel("Price Range (USD)", fontsize=12)
plt.legend(title='Company')
plt.grid(True)
plt.savefig("Daily_Price_Range_PandasOnly.png")
plt.close()

#  Pandas-Only Scatter Plot: Volume vs Adjusted Close
ax = None
for ticker in df['Ticker'].unique():
    company_df = df[df['Ticker'] == ticker]
    ax = company_df.plot(
        kind='scatter',
        x='Volume',
        y='Adj Close',
        label=ticker,
        s=100,
        alpha=0.7,
        ax=ax  
    )
plt.title("Volume vs Adjusted Close Price (Pandas Only)", fontsize=14, fontweight='bold')
plt.xlabel("Trading Volume")
plt.ylabel("Adjusted Close Price (USD)")
plt.grid(True)
plt.savefig("Volume_vs_AdjClose_PandasOnly.png")
plt.close()

# ---- Volume vs Adjusted Close Price ----
df["Date"] = pd.to_datetime(df["Date"])
ax = None
for company in df["Ticker"].unique():
    company_data = df[df["Ticker"] == company]
    
  
    ax = company_data.plot(
        kind="scatter",
        x="Volume",
        y="Adj Close",
        label=company,
        s=100,
        alpha=0.7,
        ax=ax 
    )

ax.set_title("Volume vs Adjusted Close Price", fontsize=14, fontweight='bold')
ax.set_xlabel("Trading Volume", fontsize=12)
ax.set_ylabel("Adjusted Close Price (USD)", fontsize=12)
ax.legend(title="Company")
ax.grid(True)
ax.figure.savefig("Volume_vs_AdjClose_PandasOnly.png")