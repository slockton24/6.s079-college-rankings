data = pd.read_csv('final_merged_data.csv')


cols_to_drop = [col for col in data.columns if "institution name_" in col]
cols_to_drop.append("State")
data.drop(columns=cols_to_drop, inplace=True)

pivot_data = data.pivot_table(index=['IPEDS ID'], columns='Year', values='Rank', aggfunc='first')

pivot_data.columns = [f'Rank_{year}' for year in pivot_data.columns]

pivot_data.reset_index(inplace=True)

combined_data = data.groupby('IPEDS ID').agg({
    'University Name': 'first',
    'SAT Evidence-Based Reading and Writing 25th percentile score_2018': 'max',
    'SAT Evidence-Based Reading and Writing 75th percentile score_2018': 'max',
    'SAT Math 25th percentile score_2018': 'max',
    'SAT Math 75th percentile score_2018': 'max',
    'ACT Composite 25th percentile score_2018': 'max',
    'ACT Composite 75th percentile score_2018': 'max',
    'Admissions yield - total_2018': 'max',
    'Applicants total_2018': 'max',
    'SAT Evidence-Based Reading and Writing 25th percentile score_2019': 'max',
    'SAT Evidence-Based Reading and Writing 75th percentile score_2019': 'max',
    'SAT Math 25th percentile score_2019': 'max',
    'SAT Math 75th percentile score_2019': 'max',
    'ACT Composite 25th percentile score_2019': 'max',
    'ACT Composite 75th percentile score_2019': 'max',
    'Admissions yield - total_2019': 'max',
    'Applicants total_2019': 'max',
    'SAT Evidence-Based Reading and Writing 25th percentile score_2020': 'max',
    'SAT Evidence-Based Reading and Writing 75th percentile score_2020': 'max',
    'SAT Math 25th percentile score_2020': 'max',
    'SAT Math 75th percentile score_2020': 'max',
    'ACT Composite 25th percentile score_2020': 'max',
    'ACT Composite 75th percentile score_2020': 'max',
    'Admissions yield - total_2020': 'max',
    'Applicants total_2020': 'max',
    'SAT Evidence-Based Reading and Writing 25th percentile score_2021': 'max',
    'SAT Evidence-Based Reading and Writing 75th percentile score_2021': 'max',
    'SAT Math 25th percentile score_2021': 'max',
    'SAT Math 75th percentile score_2021': 'max',
    'ACT Composite 25th percentile score_2021': 'max',
    'ACT Composite 75th percentile score_2021': 'max',
    'Admissions yield - total_2021': 'max',
    'Applicants total_2021': 'max',
    'SAT Evidence-Based Reading and Writing 25th percentile score_2022': 'mean',
    'SAT Evidence-Based Reading and Writing 75th percentile score_2022': 'mean',
    'SAT Math 25th percentile score_2022': 'mean',
    'SAT Math 75th percentile score_2022': 'mean',
    'ACT Composite 25th percentile score_2022': 'mean',
    'ACT Composite 75th percentile score_2022': 'mean',
    'Admissions yield - total_2022': 'max',
    'Applicants total_2022': 'max',
}).reset_index()

rename_dict = {
    'SAT Evidence-Based Reading and Writing 25th percentile score_2018': 'SAT RW 25th 2018',
    'SAT Evidence-Based Reading and Writing 75th percentile score_2018': 'SAT RW 75th 2018',
    'SAT Math 25th percentile score_2018': 'SAT Math 25th 2018',
    'SAT Math 75th percentile score_2018': 'SAT Math 75th 2018',
    'ACT Composite 25th percentile score_2018': 'ACT 25th 2018',
    'ACT Composite 75th percentile score_2018': 'ACT 75th 2018',
    'Admissions yield - total_2018': 'Adm Yield 2018',
    'SAT Evidence-Based Reading and Writing 25th percentile score_2019': 'SAT RW 25th 2019',
    'SAT Evidence-Based Reading and Writing 75th percentile score_2019': 'SAT RW 75th 2019',
    'SAT Math 25th percentile score_2019': 'SAT Math 25th 2019',
    'SAT Math 75th percentile score_2019': 'SAT Math 75th 2019',
    'ACT Composite 25th percentile score_2019': 'ACT 25th 2019',
    'ACT Composite 75th percentile score_2019': 'ACT 75th 2019',
    'Admissions yield - total_2019': 'Adm Yield 2019',
    'SAT Evidence-Based Reading and Writing 25th percentile score_2020': 'SAT RW 25th 2020',
    'SAT Evidence-Based Reading and Writing 75th percentile score_2020': 'SAT RW 75th 2020',
    'SAT Math 25th percentile score_2020': 'SAT Math 25th 2020',
    'SAT Math 75th percentile score_2020': 'SAT Math 75th 2020',
    'ACT Composite 25th percentile score_2020': 'ACT 25th 2020',
    'ACT Composite 75th percentile score_2020': 'ACT 75th 2020',
    'Admissions yield - total_2020': 'Adm Yield 2020',
    'SAT Evidence-Based Reading and Writing 25th percentile score_2021': 'SAT RW 25th 2021',
    'SAT Evidence-Based Reading and Writing 75th percentile score_2021': 'SAT RW 75th 2021',
    'SAT Math 25th percentile score_2021': 'SAT Math 25th 2021',
    'SAT Math 75th percentile score_2021': 'SAT Math 75th 2021',
    'ACT Composite 25th percentile score_2021': 'ACT 25th 2021',
    'ACT Composite 75th percentile score_2021': 'ACT 75th 2021',
    'Admissions yield - total_2021': 'Adm Yield 2021',
    'SAT Evidence-Based Reading and Writing 25th percentile score_2022': 'SAT RW 25th 2022',
    'SAT Evidence-Based Reading and Writing 75th percentile score_2022': 'SAT RW 75th 2022',
    'SAT Math 25th percentile score_2022': 'SAT Math 25th 2022',
    'SAT Math 75th percentile score_2022': 'SAT Math 75th 2022',
    'ACT Composite 25th percentile score_2022': 'ACT 25th 2022',
    'ACT Composite 75th percentile score_2022': 'ACT 75th 2022',
    'Admissions yield - total_2022': 'Adm Yield 2022',
}

combined_data.rename(columns=rename_dict, inplace=True)

final_data = pd.merge(combined_data, pivot_data, on=['IPEDS ID'], how='left')


final_data.to_csv('combined_university_data.csv', index=False)


print(combined_data.head())