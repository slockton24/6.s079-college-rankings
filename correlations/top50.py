import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('us_rankings_1984_2023.csv')
df.set_index('University Name', inplace=True)

# filter out columns for years before 1995
years = [str(year) for year in range(1995, 2024)]
df_filtered = df[years]
df_filtered = df_filtered.dropna()


top_50_per_year = pd.DataFrame(index=df_filtered.index)

for year in df_filtered.columns:
    year_data = df_filtered[year].nsmallest(50)
    top_50_per_year[year] = year_data

top_50_per_year.dropna(how='all', inplace=True)

plt.figure(figsize=(20, 10))
ax = sns.heatmap(top_50_per_year, annot=False, cmap='coolwarm_r', linewidths=.5)
plt.title('Heatmap of Top 50 College Rankings Over Years')
plt.xlabel('Year')
plt.ylabel('University')
ax.set_xticklabels([year[-2:] for year in top_50_per_year.columns])

plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.2)

plt.subplots_adjust(left=0.3)

plt.show()
