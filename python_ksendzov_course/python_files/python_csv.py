import csv

file_path = '/Users/a17787194/python/python/python_ksendzov_course/python_files/text_files/'
text_file_title = 'text_1.txt'
csv_file_title = 'csv_2.csv'
file_title = file_path + csv_file_title

list = ['QA', 'Automation', 'employees']

users_l = [['Maxim', 30],
           ['Artyom', 32],
           ['Sasha', 35]]
# with open(file_title, 'w') as csv_f:
#     writer = csv.writer(csv_f)
#     row = ['Elena', 20]
#     row_2 = ['Anna', 23]
#     writer.writerow(row)
#     writer.writerow(row_2)

# with open(file_title, 'a') as csv_f:
#     writer = csv.writer(csv_f)
#     writer.writerows(users_l)

# with open(file_title, 'r', newline='') as csv_f:
#     reader = csv.reader(csv_f)
#     for k in reader:
#         print(k[0])
#
#      #print(*reader)

# with open(file_title, 'w') as csv_f:
#     columns = ['Name', 'Age']
#     writer = csv.DictWriter(csv_f, fieldnames=columns)
#     writer.writeheader()
#
#     user = {"Name": "Alex",
#             "Age": 30}
#     writer.writerow(user)

# users = [{"Name": "Alex", "Age": 30},
#          {"Name": "Sasha", "Age": 32},
#          {"Name": "Irina", "Age": 35},
#          {"Name": "Olga", "Age": 39}]
# with open(file_title, 'a') as csv_f:
#     columns = ['Name', 'Age']
#     writer = csv.DictWriter(csv_f, fieldnames=columns)
#     #user = {"Name": "Alex", "Age": 30}
#     writer.writerows(users)

with open(file_title, 'r') as csv_f:
    reader = csv.DictReader(csv_f)
    line_count = 0
    for l in reader:
        print(line_count, l['Name'], l['Age'])
        line_count += 1