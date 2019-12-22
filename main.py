import pandas as pd

csv_arr = pd.read_csv('base.csv', sep = ',', encoding = "cp1251")
ex1_arr = pd.read_excel('Готовые связки-2019-06-21.xlsx')
ex2_arr = pd.read_excel('Мониторинг цен по всем спискам артикулов Priceva от 20.06.19.xlsx')
