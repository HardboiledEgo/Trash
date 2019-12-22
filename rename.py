import os
import openpyxl

filename = "D:/Python 3.6 Projects/88396/Дефицит АВД wenko новинки.xlsx"
current_exel = openpyxl.load_workbook(filename)
sheet = current_exel['Заказ']

u = 0
i = 1
B_cell = 'B' + str(i)
C_cell = 'C' + str(i)

num_value = (sheet[B_cell].value)
expect_value = (sheet[C_cell].value)

print(num_value)
print(expect_value)

print("Первый проход в два массива id и наименования")

destination_path = "D:/Python 3.6 Projects/88396/test"

arr = []
arr = os.listdir(destination_path)
print(arr)

for file_name in arr:
    if file_name.startswith(str(num_value)):
        u += 1
        os.rename(os.path.join(destination_path, file_name),
                  os.path.join(destination_path, expect_value + ' ' + str(u)
                               + file_name[-4:]))
    else:
        
