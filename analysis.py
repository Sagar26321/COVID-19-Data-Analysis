import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. SETUP & LOAD
print("Loading data...")
df = pd.read_csv('covid_data.csv')
df['date'] = pd.to_datetime(df['date'])
df.fillna(0, inplace=True)

# ---------------------------------------------------------
# GRAPH 1: GLOBAL TREND (Saved as 'covid_trend.png')
# ---------------------------------------------------------
print("Generating Graph 1: Global Trend...")
global_trend = df.groupby('date')[['new_cases']].sum().reset_index()
global_trend['ma_7'] = global_trend['new_cases'].rolling(window=7).mean()

plt.figure(figsize=(12, 6))
plt.plot(global_trend['date'], global_trend['new_cases'], color='grey', alpha=0.3, label='Daily Cases (Raw)')
plt.plot(global_trend['date'], global_trend['ma_7'], color='blue', linewidth=2, label='7-Day Average')
plt.title('Global COVID-19 Cases (Smoothed Trend)')
plt.legend()
plt.savefig('covid_trend.png')
plt.close()

# ---------------------------------------------------------
# GRAPH 2: TOP 10 COUNTRIES (Saved as 'covid_top10.png')
# ---------------------------------------------------------
print("Generating Graph 2: Top 10 Comparison...")
df_countries = df[df['continent'].notna()]
top_10 = df_countries.groupby('location')['total_cases'].max().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
plt.bar(top_10.index, top_10.values, color='firebrick')
plt.title('Top 10 Countries by Total Cases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('covid_top10.png')
plt.close()

# ---------------------------------------------------------
# GRAPH 3: MORTALITY SCATTER (Saved as 'covid_scatter.png')
# ---------------------------------------------------------
print("Generating Graph 3: Mortality Scatter...")
latest_data = df_countries.sort_values('date').groupby('location').tail(1)

plt.figure(figsize=(10, 6))
plt.scatter(latest_data['total_cases'], latest_data['total_deaths'], alpha=0.5, color='purple')
plt.title('Total Cases vs. Total Deaths (Log Scale)')
plt.xscale('log')
plt.yscale('log')
plt.grid(True, which="both", ls="--", alpha=0.2)
plt.savefig('covid_scatter.png')
plt.close()

print("\n SUCCESSFULL! All 3 graphs have been saved to your folder.")