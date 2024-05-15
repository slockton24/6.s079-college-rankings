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


df_subset = df[changes_columns].dropna()  # Ensure we only consider non-null data


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

print(f"MSE: {mse:.2f}")
print(f"R2: {r2:.2f}")
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='blue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=4)
plt.xlabel('measured')
plt.ylabel('predicted')
plt.title('actual vs predicted values')
plt.show()



# # tried to apply a square root transformation to positive features -> worse results
# for col in x.columns:
#     if (x[col] > 0).all():
#         x[col] = np.sqrt(x[col])

# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
# model = LinearRegression()
# model.fit(x_train, y_train)
# y_pred = model.predict(x_test)

# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)
# print(f"MSE-2: {mse:.2f}")
# print(f"R2-2: {r2:.2f}")