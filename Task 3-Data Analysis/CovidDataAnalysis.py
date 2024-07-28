from matplotlib import style
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Update the Path of the CSV file here as per your machine
path = r'C:\Users\HASSAN\Desktop\VS CODE\Python\DataAnalysis Pyhton\covid_worldwide2.csv'
df = pd.read_csv(path)

# DATA CLEANING
# Finding percentage of NULL VALUES from a Dataset and Plotting its Graph to visualize it
missing_percentages = (df.isna().sum().sort_values(ascending=False) / len(df)) * 100

# Create the first figure
fig1, axs1 = plt.subplots(2, 2, figsize=(15, 25))
fig1.suptitle('Figure 1: COVID-19 Data Analysis Part 1', fontsize=22, fontweight='bold')

# Subplot 1: Missing Values
missing_percentages.plot(kind='barh', width=0.9, ax=axs1[0, 0])
axs1[0, 0].set_xlabel('Missing values(%)', fontweight='bold', fontsize=8)
axs1[0, 0].set_ylabel('Columns in Dataset', fontweight='bold', fontsize=8)
axs1[0, 0].set_title('Missing or Null Values', fontsize=15, fontweight='bold', color='black')

# Subplot 2: Missing Values (Non-zero)
missing_percentages_notZero = missing_percentages[missing_percentages != 0]
missing_percentages_notZero.plot(kind='barh', ax=axs1[0, 1])
axs1[0, 1].set_xlabel('Missing values(%)', fontweight='bold', fontsize=8)
axs1[0, 1].set_ylabel('Columns in Dataset', fontweight='bold', fontsize=8)
axs1[0, 1].set_title('Missing or Null Values (after filtering)', fontsize=15, fontweight='bold', color='black')

# Dropping Null Values
df.dropna(inplace=True)

# Saving cleaned data to a new CSV file. Adjust this path according to your machine.
cleaned_path = r'C:\Users\HASSAN\Desktop\VS CODE\Python\DataAnalysis Pyhton\cleaned_covid_worldwide2.csv'
df.to_csv(cleaned_path, index=False)

# Making columns type numeric as they have commas in it
df['Total Deaths'] = pd.to_numeric(df['Total Deaths'].str.replace(',', ''), errors='coerce')
df['Total Cases'] = pd.to_numeric(df['Total Cases'].str.replace(',', ''), errors='coerce')
df['Total Recovered'] = pd.to_numeric(df['Total Recovered'].str.replace(',', ''), errors='coerce')
df['Active Cases'] = pd.to_numeric(df['Active Cases'].str.replace(',', ''), errors='coerce')
df['Total Test'] = pd.to_numeric(df['Total Test'].str.replace(',', ''), errors='coerce')
df['Population'] = pd.to_numeric(df['Population'].str.replace(',', ''), errors='coerce')

# Plotting top 20 countries according to the number of test cases reported
country_by_cases = df.groupby('Country')['Total Cases'].sum()
country_by_cases_sorted = country_by_cases.sort_values(ascending=False)
top_20_countries_byCases = country_by_cases_sorted[:20]

top_20_countries_byCases.plot(kind='barh', ax=axs1[1, 0])
axs1[1, 0].set_ylabel('Countries', fontweight='bold', fontsize=8)
axs1[1, 0].set_xlabel('Cases Reported', fontweight='bold', fontsize=8)
axs1[1, 0].set_title('Top 20 Countries with maximum Covid Cases reported', fontsize=10, fontweight='bold', color='black')

# Plotting top 20 countries according to the minimum number of test cases reported
country_by_min_cases = df.groupby('Country')['Total Cases'].sum()
country_by_min_cases_sorted = country_by_min_cases.sort_values(ascending=True)
top_20_countries_by_min_Cases = country_by_min_cases_sorted[:20]

top_20_countries_by_min_Cases.plot(kind='barh', ax=axs1[1, 1])
axs1[1, 1].set_ylabel('Countries', fontweight='bold', fontsize=8)
axs1[1, 1].set_xlabel('Cases Reported', fontweight='bold', fontsize=8)
axs1[1, 1].set_title('Top 20 Countries with minimum Covid Cases reported', fontsize=10, fontweight='bold', color='black')

# Create the second figure
fig2, axs2 = plt.subplots(2, 2, figsize=(15, 25))
fig2.suptitle('Figure 2: COVID-19 Data Analysis Part 2', fontsize=22, fontweight='bold')

# Plotting top 20 countries with maximum number of Deaths
country_by_deaths= df.groupby('Country')['Total Deaths'].sum()
country_by_deaths_sorted=country_by_deaths.sort_values(ascending=False)
top_20_countries_byDeath= country_by_deaths_sorted[:20]
print(top_20_countries_byDeath)
top_20_countries_byDeath.plot(kind='bar', ax=axs2[0, 0])
axs2[0, 0].set_xlabel('Countries', fontweight='bold', fontsize=8)
axs2[0, 0].set_ylabel('Total Deaths', fontweight='bold', fontsize=8)
axs2[0, 0].set_title('Top 20 Countries with maximum deaths', fontsize=15, fontweight='bold', color='black')
axs2[0, 0].tick_params(axis='x', labelsize=5)

# Plotting top 20 countries with minimum number of Deaths
country_by_min_deaths= df.groupby('Country')['Total Deaths'].sum()
country_by_min_deaths_sorted=country_by_deaths.sort_values(ascending=True)
top_20_countries_bymin_Death= country_by_min_deaths_sorted[:20]
print(top_20_countries_bymin_Death)
top_20_countries_bymin_Death.plot(kind='bar', ax=axs2[0, 1])
axs2[0, 1].set_xlabel('Countries', fontweight='bold', fontsize=8)
axs2[0, 1].set_ylabel('Total Deaths', fontweight='bold', fontsize=8)
axs2[0, 1].set_title('Top 20 Countries with minimum deaths', fontsize=15, fontweight='bold', color='black')
axs2[0, 1].tick_params(axis='x', labelsize=5)

# Plotting top 20 countries where there was maximum recovery from covid
country_by_recovery= df.groupby('Country')['Total Recovered'].sum()
country_by_recovery_sorted=country_by_recovery.sort_values(ascending=False)
top_20_countries_byRecovery= country_by_recovery_sorted[:20]
print(top_20_countries_byRecovery)
top_20_countries_byRecovery.plot(kind='bar', ax=axs2[1, 0])
axs2[1, 0].set_xlabel('Countries', fontweight='bold', fontsize=8)
axs2[1, 0].set_ylabel('Total Recovered', fontweight='bold', fontsize=8)
axs2[1, 0].set_title('Top 20 Countries with maximum recovery', fontsize=15, fontweight='bold', color='black')
axs2[1, 0].tick_params(axis='x', labelsize=5)

# Plotting top 20 countries where there was minimum recovery from covid
country_by_min_recovery= df.groupby('Country')['Total Recovered'].sum()
country_by_min_recovery_sorted=country_by_min_recovery.sort_values(ascending=True)
top_20_countries_by_min_Recovery= country_by_min_recovery_sorted[:20]
print(top_20_countries_by_min_Recovery)
top_20_countries_by_min_Recovery.plot(kind='bar', ax=axs2[1, 1])
axs2[1, 1].set_xlabel('Countries', fontweight='bold', fontsize=8)
axs2[1, 1].set_ylabel('Total Recovered', fontweight='bold', fontsize=8)
axs2[1, 1].set_title('Top 20 Countries with minimum recovery', fontsize=15, fontweight='bold', color='black')
axs2[1, 1].tick_params(axis='x', labelsize=5)

# Create the third figure
fig3, axs3 = plt.subplots(2, 2, figsize=(15, 25))
fig3.suptitle('Figure 3: COVID-19 Data Analysis Part 3', fontsize=22, fontweight='bold')

# Plotting countries having maximum number of Active Cases
country_by_active_cases= df.groupby('Country')['Active Cases'].sum()
country_by_active_cases_sorted=country_by_active_cases.sort_values(ascending=False)
top_20_countries_by_active_cases= country_by_active_cases_sorted[:20]
print(top_20_countries_by_active_cases)
top_20_countries_by_active_cases.plot(kind='barh', ax=axs3[0, 0])
axs3[0, 0].set_xlabel('Active Cases', fontweight='bold', fontsize=8)
axs3[0, 0].set_ylabel('Countries', fontweight='bold', fontsize=8)
axs3[0, 0].set_title('Top 20 Countries with maximum Active Cases', fontsize=15, fontweight='bold', color='black')

# Plotting countries having minimum number of Active Cases
country_by_minactive_cases= df.groupby('Country')['Active Cases'].sum()
country_by_minactive_cases_sorted=country_by_minactive_cases.sort_values(ascending=True)
top_20_countries_by_minactive_cases= country_by_minactive_cases_sorted[:20]
print(top_20_countries_by_minactive_cases)
top_20_countries_by_minactive_cases.plot(kind='barh', ax=axs3[0, 1])
axs3[0, 1].set_xlabel('Active Cases', fontweight='bold', fontsize=8)
axs3[0, 1].set_ylabel('Countries', fontweight='bold', fontsize=8)
axs3[0, 1].set_title('Top 20 Countries with minimum Active Cases', fontsize=15, fontweight='bold', color='black')

# Summarizing the Data Analysis
# Plotting top 20 Countries with Cases Reported, Deaths
# Plotting countries having minimum number of Active Cases
top_20_countries_byCases.plot(kind='line',ax=axs3[1, 0],label='Cases')
top_20_countries_byDeath.plot(kind='line',ax=axs3[1, 0],label='Deaths')
top_20_countries_byRecovery.plot(kind='line',ax=axs3[1, 0],label='Recovery')

axs3[1, 0].legend()
axs3[1, 0].set_xlabel('Countries', fontweight='bold', fontsize=8)
axs3[1, 0].set_ylabel('Counts', fontweight='bold', fontsize=8)
axs3[1, 0].set_title('Top 20 Countries by Cases,Deaths & Recovery', fontsize=15, fontweight='bold', color='black', loc='center')

top_20_countries_byCases.plot(kind='line',ax=axs3[1, 1],label='Cases')
top_20_countries_by_active_cases.plot(kind='line',ax=axs3[1, 1],label='Active Cases')

axs3[1, 1].legend()
axs3[1, 1].set_xlabel('Countries', fontweight='bold', fontsize=8)
axs3[1, 1].set_ylabel('Counts', fontweight='bold', fontsize=8)
axs3[1, 1].set_title('Top 20 Countries by Total Cases & Active Cases', fontsize=15, fontweight='bold', color='black', loc='center')

# Adjust the layout
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
