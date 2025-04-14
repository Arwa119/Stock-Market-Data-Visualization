import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
import os
# inter company comaparison

# ---- open prices of companies over time ----
main_folder = "data"
if not os.path.exists(main_folder):
     os.makedirs(main_folder)

inter_company = os.path.join(main_folder,'inter_company')
if not os.path.exists(inter_company):
        os.makedirs(inter_company)

df = pd.read_csv('stocks.csv')
df['Date'] = pd.to_datetime(df['Date'])

plt.figure(figsize=(12,6))
sns.set_style("whitegrid")
sns.lineplot( data = df , x='Date', y ='Open' , hue='Ticker',marker='o')
plt.xlabel('Date',fontsize=12,fontweight='bold')
plt.ylabel('Opening Prices(USD)',fontsize=12,fontweight='bold')
plt.title('Opening Prices Over Time', fontsize=16, fontweight='bold')
plt.legend(title='Company' ,loc="upper right")
plt.savefig(f"{inter_company}/OpeningPrices_of_Companies.png")



# ---- closing prices of comapnies over time ----

plt.figure(figsize=(12,6))
sns.set_style("whitegrid")
sns.lineplot(data=df,x='Date',y='Close', hue='Ticker',marker='o')
plt.legend(title='Company' ,loc="upper right")
plt.title('Closing Prices Over Time', fontsize=16,fontweight='bold')
plt.xlabel('Date',fontsize=12,fontweight='bold')
plt.ylabel('Closing Prices(USD)',fontsize=12,fontweight='bold')
plt.savefig(f"{inter_company}/Closing_Prices.png")


# ---- Highest Prices Over Time ----

plt.figure(figsize=(12,6))
sns.set_style("whitegrid")
sns.lineplot(data=df,x='Date',y='High', hue='Ticker',marker='o')
plt.legend(title='Company' ,loc="upper right")
plt.title('Highest Price Per Day', fontsize=16,fontweight='bold')
plt.xlabel('Date',fontsize=12,fontweight='bold')
plt.ylabel('Highest Price(USD)',fontsize=12,fontweight='bold')
plt.savefig(f"{inter_company}/Highest_Prices.png")

# ---- Lowest Price Over Time ----

plt.figure(figsize=(12,6))
sns.set_style("whitegrid")
sns.lineplot(data=df,x='Date',y='Low', hue='Ticker',marker='o')
plt.legend(title='Company' ,loc="upper right")
plt.title('Lowest Price Per Day', fontsize=16,fontweight='bold')
plt.xlabel('Date',fontsize=12,fontweight='bold')
plt.ylabel('Lowest Price(USD)',fontsize=12,fontweight='bold')
plt.savefig(f"{inter_company}/Lowest_Prices.png")


# ---- Adj Close Over Time----

plt.figure(figsize=(12,6))
sns.lineplot(data=df, x='Date',y='Adj Close',hue='Ticker',marker='o')
sns.set_style('whitegrid')
plt.legend(title='Company',loc='upper right')
plt.title('Adjusted Clsoe Over Time', fontsize=16,fontweight='bold')
plt.xlabel('Date',fontsize=12,fontweight='bold')
plt.ylabel('Adjusted Close(USD)',fontsize=12,fontweight='bold')
plt.savefig(f"{inter_company}/Adj_Close.png")


# ---- Volume of stock sold ----

plt.figure(figsize=(12,6))
sns.lineplot(data=df, x='Date',y='Volume',hue='Ticker',marker='o')
sns.set_style('whitegrid')
plt.legend(title='Company',loc='upper right')
plt.title('Volume Of Shares Traded Per Company Per Day', fontsize=16,fontweight='bold')
plt.xlabel('Date', fontsize=12,fontweight='bold')
plt.ylabel('Volume', fontsize=12,fontweight='bold')
plt.savefig(f"{inter_company}/Volume.png")



# -----COMPANY WISE DATA VISUALIZATION----

companies = df['Ticker'].unique()
for company in companies:
    df_cmp = df[df['Ticker']==company]\
    
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


    