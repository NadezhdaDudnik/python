file_path = 'python/python/python_ksendzov_course/python_files/text_files/'
text_file_title = 'text_1.txt'
file_title = file_path + text_file_title
# f = open(file_title, 'w')
# f.write('Hello file')
# f.close()

list = ['QA', 'Automation', 'employees']
# with open(file_title, 'w', encoding='utf-8') as file:
# #with open(file_title, 'x', encoding='utf-8') as file:
# #with open(file_title, 'a', encoding='utf-8') as file:
#     #file.write('Hello QA!')
#     #file.write(str(list))
#     #file.writelines(list)
#     #file.write('\n'.join(list))
#
#     for n in range(0, 10):
#         for i in list:
#             w_line = str(n) + '_' + i
#             file.writelines(i)
#             file.write('\n')

    # for i in list:
    #     # file.write(i)
    #     # file.write('\n')
    #     file.writelines(i)
    #     file.write('\n')

with open(file_title, 'r') as file:
    #file1 = file.read()
    #file1 = file.read(10)

    file1 = file.readlines()
    print(file1)
    #print(len(file1))

    for lines in file1:
        #print(lines)
        print(lines.rstrip())