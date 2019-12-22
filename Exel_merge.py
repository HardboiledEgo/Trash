import pandas as pd

csv_file = 'base.csv'
#excel_file_1 = 'pd_1.xlsx'
#excel_file_2 = 'pd_2.xlsx'
expect_excel = pd.DataFrame()

csv_1 = pd.DataFrame(pd.read_csv(csv_file, encoding = '1251', sep = ';'))

#pd_1 = pd.DataFrame(pd.read_excel(excel_file_1))

#pd_2 = pd.DataFrame(pd.read_excel(excel_file_2))

#pd_1 = pd_1.drop(pd_1.columns[[0, 1, 2, 3, 5, 6, 7, 9, 10, 12, 13, 14, 15, 17, 18, 19, 20, 21]], axis=1)
#pd_1.to_excel('result.xlsx', index = False)

#print(csv_1.iloc[[14, 12, 106], [3, 4]])