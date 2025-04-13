import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

# inter company comaparison

# ---- open prices of companies over time ----

df = pd.read_csv('stocks.csv')
df['Date'] = pd.to_datetime(df['Date'])

# plt.figure(figsize=(12,6))
# sns.set_style("whitegrid")
# sns.lineplot( data = df , x='Date', y ='Open' , hue='Ticker',marker='o')
# plt.xlabel('Date',fontsize=12,fontweight='bold')
# plt.ylabel('Opening Prices(USD)',fontsize=12,fontweight='bold')
# plt.title('Opening Prices Over Time', fontsize=16, fontweight='bold')
# plt.legend(title='Company' ,loc="upper right")
# # plt.savefig('OpeningPrices_of_Companies.png')
# plt.show()


# ---- closing prices of comapnies over time ----

# plt.figure(figsize=(12,6))
# sns.set_style("whitegrid")
# sns.lineplot(data=df,x='Date',y='Close', hue='Ticker',marker='o')
# plt.legend(title='Company' ,loc="upper right")
# plt.title('Closing Prices Over Time', fontsize=16,fontweight='bold')
# plt.xlabel('Date',fontsize=12,fontweight='bold')
# plt.ylabel('Closing Prices(USD)',fontsize=12,fontweight='bold')
# # plt.savefig('Closing_Prices.png')
# plt.show()

# ---- Highest Prices Over Time ----
# plt.figure(figsize=(12,6))
# sns.set_style("whitegrid")
# sns.lineplot(data=df,x='Date',y='High', hue='Ticker',marker='o')
# plt.legend(title='Company' ,loc="upper right")
# plt.title('Highest Price Per Day', fontsize=16,fontweight='bold')
# plt.xlabel('Date',fontsize=12,fontweight='bold')
# plt.ylabel('Highest Price(USD)',fontsize=12,fontweight='bold')
# plt.savefig('Highest_Prices.png')
# plt.show()

# ---- Lowest Price Over Time ----
# plt.figure(figsize=(12,6))
# sns.set_style("whitegrid")
# sns.lineplot(data=df,x='Date',y='Low', hue='Ticker',marker='o')
# plt.legend(title='Company' ,loc="upper right")
# plt.title('Lowest Price Per Day', fontsize=16,fontweight='bold')
# plt.xlabel('Date',fontsize=12,fontweight='bold')
# plt.ylabel('Lowest Price(USD)',fontsize=12,fontweight='bold')
# plt.savefig('Lowest_Prices.png')
# plt.show()

# ---- Adj Close Over Time----
# plt.figure(figsize=(12,6))
# sns.lineplot(data=df, x='Date',y='Adj Close',hue='Ticker',marker='o')
# sns.set_style('whitegrid')
# plt.legend(title='Company',loc='upper right')
# plt.title('Adjusted Clsoe Over Time', fontsize=16,fontweight='bold')
# plt.xlabel('Date',fontsize=12,fontweight='bold')
# plt.ylabel('Adjusted Close(USD)',fontsize=12,fontweight='bold')
# plt.savefig('Adj_Close.png')
# plt.show()

# ---- Volume of stock sold ----

plt.figure(figsize=(12,6))
sns.lineplot(data=df, x='Date',y='Volume',hue='Ticker',marker='o')
sns.set_style('whitegrid')
plt.legend(title='Company',loc='upper right')
plt.title('Volume Of Shares Traded Per Company Per Day', fontsize=16,fontweight='bold')
plt.xlabel('Date', fontsize=12,fontweight='bold')
plt.ylabel('Volume', fontsize=12,fontweight='bold')
# plt.savefig('Volume.png')
plt.show()
