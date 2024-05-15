import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('combined_university_data.csv')

# Caltech jumped from 9 to 1 to 4 from 1999 to 2001

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

# Add columns for year-over-year differences
# years = [2019, 2020, 2021, 2022]
# for metric in score_metrics:
#     for year in range(2019, 2023):
#         previous_year_metric = f"{metric}{year - 1}"
#         current_year_metric = f"{metric}{year}"
#         if previous_year_metric in df.columns and current_year_metric in df.columns:
#             print(f"Change in {metric}{year}")
#             df[f"Change in {metric}{year}"] = df[current_year_metric] - df[previous_year_metric]

years = [2019, 2020, 2021, 2022]
for metric in score_metrics:
    previous_year_metric = f"{metric}2018"
    current_year_metric = f"{metric}2022"
    if previous_year_metric in df.columns and current_year_metric in df.columns:
        df[f"Change in {metric}"] = df[current_year_metric] - df[previous_year_metric]
    else:
        print("column not found")


correlation_averages = {}
relevant_columns = []
# for year in years:
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

df_subset = df[changes_columns].dropna()



correlation_results = {}
for col in df_subset.columns:
    if col != 'Change in Rank_':  # Avoid comparing the same column
        correlation, p_value = pearsonr(df_subset['Change in Rank_'], df_subset[col])
        correlation_results[col] = (correlation, p_value)

for metric, results in correlation_results.items():
    print(f"{metric}: Correlation: {results[0]:.3f}, P-value: {results[1]:.4f}")


correlations, p_values = zip(*correlation_results.values())  # Unpack results into separate tuples
metrics = list(correlation_results.keys())

x = df_subset[[  # Ensure these columns are the correct metrics from your dataset
    'Change in SAT RW 25th ',
    'Change in SAT RW 75th ',
    'Change in SAT Math 25th ',
    'Change in SAT Math 75th ',
    'Change in ACT 25th ',
    'Change in ACT 75th ',
    'Change in Adm Yield ',
    'Change in Applicants total_'
]]
y = df_subset['Change in Rank_']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MES: {mse:.2f}")
print(f"R2: {r2:.2f}")

plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='blue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=4)
plt.xlabel('measured')
plt.ylabel('predicted')
plt.title('actual vs predicted values')
plt.show()
