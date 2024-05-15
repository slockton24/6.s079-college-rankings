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
top_rank_threshold =25
rank_columns = [f'Rank_{year}' for year in range(2018, 2023)]

rank_data = df[rank_columns]

df = df[(rank_data <= top_rank_threshold).any(axis=1)]

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



correlation_results = {}

change_rank_col = f'Change in Rank_'
df[change_rank_col] = pd.to_numeric(df[change_rank_col], errors='coerce')
df.dropna(subset=[change_rank_col], inplace=True)
print(df.columns)

change_columns = [col for col in df.columns if col.startswith('Change') and col != change_rank_col]
print(change_columns)

for col in change_columns:
    if col != change_rank_col:
        df[col] = pd.to_numeric(df[col], errors='coerce')
        df.dropna(subset=[col], inplace=True)

        if df[col].notna().all():
            correlation, p_value = pearsonr(df[change_rank_col], df[col])
            correlation_results[col] = (correlation, p_value)

if correlation_results:
    correlations, p_values = zip(*correlation_results.values())
    plt.figure(figsize=(10, 8))
    sns.heatmap(pd.DataFrame([correlations, p_values], columns=change_columns, index=['Correlation', 'P-value']),
                annot=True, fmt=".3f", cmap='coolwarm')
    plt.title(f'Correlation and P-value Heatmap for Changes in Rank and Admission statistics 2018-2022')
    plt.show()
else:
    print(f"No valid data for correlation")