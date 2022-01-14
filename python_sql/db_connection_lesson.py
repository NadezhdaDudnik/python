# psycopg2 - библиотека для работы с базами данных postregSQL
import psycopg2

# connect to database - из данной библиотеки есть команда connect
conn = psycopg2.connect(dbname='qa_ddldb_23_85',
                        user='user_23_85',
                        password='123',
                        host='159.69.151.133',
                        port='5056')

cursor = conn.cursor();

#как узнать в таблице какие столбцы
if conn:
    print('Connection qa_ddldb_23_85 - ')
    select_query_for_table = 'select * from public.employees;'
    cursor.execute(select_query_for_table)
    print(cursor.description[1][0])
    column_names = [desc[0] for desc in cursor.description]
    for i in column_names:
        print(i)
    conn.commit()

if conn:
    print('Connection qa_ddldb_23_85')
    select_query = 'select * from public.employees;'
    execute_query = cursor.execute(select_query);
    # fetchall() выполняет и пакует все , что ушло в базу и все, что пришло с базы
    get_query_result = cursor.fetchall();
    print('execute_query', get_query_result)

    # появился кортеж
    for i in get_query_result:
        print('id = ', i[0], 'employee_name =', i[1]);

for i in range(0, 10):
    if conn:
        print('Connection Insert qa_ddldb_23_85 table employee_salary')
        employee_id = str(170 + i);
        salary_id = str(1 + i)
        insert_query = 'insert into public.employee_salary(employee_id, salary_id) ' \
                       'values(' + employee_id + ',' + salary_id + ');'
        cursor.execute(insert_query);
        conn.commit();

if conn:
    select_query = 'select * from public.employee_salary;'
    execute_query = cursor.execute(select_query);
    # fetchall() выполняет и пакует все , что ушло в базу и все, что пришло с базы
    get_query_result = cursor.fetchall();
    print('execute_query', get_query_result)
    for i in get_query_result:
        print('id = ', i[0], 'employee_id =', i[1], 'salary_id =', i[2]);

for j in range(0, 10):
    if conn:
        print('Connection Insert qa_ddldb_23_85 table role_name');
        role_name = "'Python_" + str(j) + "'";
        insert_query = 'insert into public.roles(role_name) ' \
                       'values(' + role_name + ');'
        cursor.execute(insert_query);
        conn.commit();

if conn:
    select_query_role = 'select * from public.roles;'
    execute_query_role = cursor.execute(select_query_role);
    # fetchall() выполняет и пакует все , что ушло в базу и все, что пришло с базы
    get_query_result_role = cursor.fetchall();
    print('execute_query_role', get_query_result_role)
    for i in get_query_result_role:
        print('id_role = ', i[0], 'role_name =', i[1]);

cursor.close();
