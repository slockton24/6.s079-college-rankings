import pandas as pd

# Function to prepare each year's data
def prepare_data(df, year):
    # Add year suffix to each column except for 'unitid' and 'year'
    df = df.rename(columns={col: f"{col}_{year}" for col in df.columns if col not in ['unitid', 'year']})
    # Standardize 'unitid' and 'year' column names
    df.rename(columns={'unitid': 'IPEDS ID', 'year': 'Year'}, inplace=True)
    # Ensure 'Year' is an integer (if it's read as a string or float)
    df['Year'] = df['Year'].astype(int)
    return df

# Load admissions data
admissions_data_2022 = prepare_data(pd.read_csv('2022/2022.csv'), 2022)
admissions_data_2021 = prepare_data(pd.read_csv('2021/2021.csv'), 2021)
admissions_data_2020 = prepare_data(pd.read_csv('2020/2020.csv'), 2020)
admissions_data_2019 = prepare_data(pd.read_csv('2019/2019.csv'), 2019)
admissions_data_2018 = prepare_data(pd.read_csv('2018/2018.csv'), 2018)

# Load rankings data
rankings_data = pd.read_csv('available_rankings.csv')
rankings_data['IPEDS ID'] = rankings_data['IPEDS ID'].astype(float)
rankings_data['Year'] = rankings_data['Year'].astype(int)

# Perform the merging
final_data = rankings_data
for df in [admissions_data_2018, admissions_data_2019, admissions_data_2020, admissions_data_2021, admissions_data_2022]:
    final_data = pd.merge(final_data, df, on=['IPEDS ID', 'Year'], how='left')

# Check the results
print(final_data.head())

# Save the final merged data
final_data.to_csv('final_merged_data.csv', index=False)
