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



