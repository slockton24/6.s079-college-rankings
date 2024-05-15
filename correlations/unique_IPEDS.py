import pandas as pd

df = pd.read_csv('available_rankings.csv')
df['IPEDS ID'] = pd.to_numeric(df['IPEDS ID'], errors='coerce').fillna(0).astype(int)
unique_ipeds = df['IPEDS ID'].unique()

unique_ipeds_string = ', '.join(map(str, unique_ipeds))

with open('unique_ipeds_ids.txt', 'w') as f:
    f.write(unique_ipeds_string)