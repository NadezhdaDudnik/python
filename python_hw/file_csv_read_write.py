import csv
file_path = '//'
file_csv = 'csv_lesson_8_header.csv'

path_csv = file_path + file_csv;

users_list =[
    ['Vadim', 32],
    ['Alexey', 34],
    ['Julia', 19]
]

users_dict = [
    {'name': 'Vadim', 'age': 32},
    {'name': 'Nadin', 'age': 35},
    {'name': 'Yulia', 'age': 38}
]

#with open(path_csv, 'w') as cf:
 #   writer = csv.writer(cf);
 #   writer.writerows(users_list)


with open(path_csv, 'w') as csv_f:
    columns = ['name', 'age']
    writer = csv.DictWriter(csv_f, fieldnames=columns)
    writer.writeheader();
    row_1 = {'name': 'Vlas', 'age': 25}
    writer.writerow(row_1)

#with open(file_csv, 'a') as csv_file:
#    writer_csv =csv.writer(csv_file)
#    row_1 = ['Vlas', 25]
#    writer_csv.writerow(row_1)

with open(path_csv, 'w') as csv_f:
    columns = ['name', 'age']
    writer = csv.DictWriter(csv_f, fieldnames=columns)
    writer.writeheader();
    writer.writerows(users_dict)

with open(path_csv, 'r') as csv_f:
    reader = csv.DictReader(csv_f)
    line_count = 0
    age_list = []
    for row in reader:
        print(row['name'], row['age']);
        print(row)
        age_list.append(row['age'])
    print(age_list)
