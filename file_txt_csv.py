import csv

file_path = '/Users/a17787194/python/python/'
file_name = 'txt_lesson_7.txt'
file_csv = 'txt_lesson_7.csv'

path = file_path + file_name;
path_csv = file_path + file_csv;
names_list = ['Alina', 'Denis', 'Vadim', 'Katya']
name_age = [];

with open(path, 'w') as txt_file:
    txt_file.write('\n'.join(names_list));

#перезаписывание всего файла - w -write
f = open(path, 'w');
f.write('Hello\nMoscow ');
f.write('Hello Moscow\n');
f.close();

with open(path, 'a') as txt_file:
    name = 'Nadin ';
    surname = 'protestinginfo\n'
    full_name = name + surname;
    txt_file.write(full_name);

#добавление информации в файл = a - add
with open(path, 'a') as txt_file:
    name = 'Nadya ';
    surname = 'QA\n'
    full_name = name + surname;
    txt_file.write(full_name);

#input - ввод данных с клавиатуры
with open(path, 'a') as txt_file:
    name = input('name: ');
    surname = input('surname: \n');
    full_name = name + surname;
    txt_file.write(full_name);

#через список
with open(path, 'a') as txt_file:
    for i in names_list:
        txt_file.write(i);
        txt_file.write('\n')

#чтение файла
with open(path, 'r') as txt_file:
    #read_file = txt_file.read();
    read_file = txt_file.readlines();
    for i in read_file:
        print(i.rstrip(), type(i))

#csv файл
users_list = [
    ['vadim', 32],
    ['alexey', 34],
    ['julia', 18],
]

new_user_lists =[]
for item in range(0, 100):
    for ul_item in users_list:
        name_age = []
        new_name = ul_item[0] + ' ' + str(item)
        new_age = 10 + item;
        name_age.append(new_name);
        name_age.append(new_age);
        #print(new_name, new_age)
        new_user_lists.append(name_age)
for ii in new_user_lists:
    print(ii)

with open(path_csv, 'w') as csv_file:
    writer = csv.writer(csv_file);
    writer.writerows(new_user_lists);


