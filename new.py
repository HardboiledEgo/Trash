
import openpyxl

filename = "D:\88396\Дефицит АВД wenko новинки.xlsx"
current_exel = openpyxl.load_workbook(filename)
sheet = current_exel['Заказ']

B_dictionary = []
C_dictionary = []

i = 0
num_value = 0

while num_value != None:

    i += 1

    B_cell = 'B' + str(i)
    C_cell = 'C' + str(i)

    num_value = (sheet[B_cell].value)
    expect_value = (sheet[C_cell].value)

    if num_value != None:
        B_dictionary.append(num_value)
        C_dictionary.append(expect_value)
            
    print(B_dictionary)
    print(C_dictionary)
