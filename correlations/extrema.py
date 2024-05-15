import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from scipy.stats import pearsonr
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


df = pd.read_csv('combined_university_data.csv')
# top_rank_threshold =25
rank_columns = [f'Rank_{year}' for year in range(2018, 2023)]

rank_data = df[rank_columns]

# df = df[(rank_data <= top_rank_threshold).any(axis=1)]

score_metrics = [
    'Rank_',
    'SAT RW 25th ',
    'SAT RW 75th ',
    'SAT Math 25th ',
    'SAT Math 75th ',
    'ACT 25th ',
    'ACT 75th ',
    'Adm Yield ',
    'Applicants total_'
]


for metric in score_metrics:
    previous_year_metric = f"{metric}2018"
    current_year_metric = f"{metric}2022"
    if previous_year_metric in df.columns and current_year_metric in df.columns:
        df[f"Change in {metric}"] = df[current_year_metric] - df[previous_year_metric]
    else:
        print("column not found")


changes_columns = [
    f'Change in Rank_',
    f'Change in SAT RW 25th ',
    f'Change in SAT RW 75th ',
    f'Change in SAT Math 25th ',
    f'Change in SAT Math 75th ',
    f'Change in ACT 25th ',
    f'Change in ACT 75th ',
    f'Change in Adm Yield ',
    f'Change in Applicants total_'
]


columns_to_analyze = df.columns.drop(['IPEDS ID', 'University Name'])
change_columns = [col for col in columns_to_analyze if col.startswith('Change')]




for col in columns_to_analyze:
    top_values = df.nlargest(5, col)
    print(f"Top 5 values for {col}:")
    for index, row in top_values.iterrows():
        print(f"  {row[col]} associated with {row['University Name']}")

rank_columns = [col for col in df.columns if col.startswith('Rank_')]
for col in rank_columns:
    bottom_value = df[col].min()
    associated_universities = df.loc[df[col] == bottom_value, 'University Name']
    print(f"Lowest value for {col} is {bottom_value}, associated with:")
    for university in associated_universities:
        print(f"  {university}")


### examining princetons stats
sat_act_columns = [col for col in df.columns if ('SAT' in col or 'ACT' in col) and ('2018' in col) and ('Change' not in col)]  # example for the year 2018
print(df.columns)
print(sat_act_columns)

columns_of_interest = ['University Name'] + sat_act_columns

df_filtered = df[columns_of_interest]

for col in sat_act_columns:
    df_filtered[f'Rank {col}'] = df_filtered[col].rank(ascending=False, method='min')

princeton_ranks = df_filtered[df_filtered['University Name'].str.contains("Princeton", case=False, na=False)]
princeton_ranks.to_csv('princeton_sat_act_ranks.csv', index=False)


print(princeton_ranks)