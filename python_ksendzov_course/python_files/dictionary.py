import json

path = '//'
file_title = '../python_hw/python_json_lesson.json'

full_name =path + file_title
dict_item = {}
dict_item = {
    1: 'Nadin',
    2: 'Alina',
    3: {'name': 'Victor', 'age': '31', 'salary': 1000},
    4: [1, 2, 3, 4, 8]
};

print(dict_item[3])
print(dict_item)
print(1, ':', dict_item[1]);
print(3, ':', dict_item[3]['name'], dict_item[3]['age']);

x = dict_item.get(3).get('salary');
print(x);

dict_item['city'] = 'Moscow'
print(dict_item);
print(dict_item);

dict_item[1] = 'Georgy'
print(dict_item, len(dict_item));

#del dict_item[2]
#print(dict_item);

#dict_item.popitem()
#print(dict_item);

#dict_item.pop('city')
#print(dict_item);

#dict_item.clear()
#print(dict_item);

dict_2 = dict_item
print('dict_2', dict_2)

dict_2['city'] = 'Dnepr'

dict_3 = dict_item
print('dict_3', dict_3)

dict_4 = dict_item.copy()
print('dict_4', dict_4)

for key, value in dict_item.items():
    #print('key:', key, 'value:', value)
    #print('key:', key)
    print('item:', dict_item[key]);

with open(full_name, 'w') as jf:
    json.dump(dict_item, jf);

with open(full_name, 'r') as jf:
    json_data = jf.read()
    json_object = json.loads(json_data);
    print('json_data:', json_data, type(json_data));
    print('json_object:', json_object, type(json_object));
