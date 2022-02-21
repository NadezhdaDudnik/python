import csv
import names

first_task = open('empty.csv', 'w', newline='')
first_task.close()

file_path = '/Users/a17787194/python/python/python_ksendzov_course/python_files/text_files/'
csv_file_title = 'digits.csv'
file_title = file_path + csv_file_title

#Вариант 1. Создать digits.csv файл с 1-м полем, в котором будут 150 строк с числами от 0 до 150
with open(file_title, 'w', encoding='utf-8') as digits_f:
    digits = csv.writer(digits_f)
    for n in range(1, 151):
        digits.writerow({str(n)})

#_________________________________________-
names_file_title = 'names.csv'
namef_title = file_path + names_file_title
#Вариант 1. Создать names.csv файл с 1-м полем, в котором будут 100 строк с разными именами
with open(namef_title, 'w', encoding='utf-8') as names_f:
    name_random = csv.writer(names_f)
    for k in range(0, 100):
        name_random.writerow({names.get_first_name()})

