import psycopg2

conn = psycopg2.connect(dbname = 'qa_ddldb_23_85',
                        user = 'user_23_85',
                        password = '123',
                        host = '159.69.151.133',
                        port = '5056')

cursor = conn.cursor();
if conn:
    print('Connection qa_ddldb_23_85')
    select_query = 'select * from public.employees;'
    ececute_query = cursor.execute(select_query);
    # fetchall() выполняет и пакует , что пришло с базы
    get_query_result = cursor.fetchall();
    print('ececute_query', get_query_result)

    for i in get_query_result:
        print('id = ', i[0], 'employee_name =', i[1]);


if conn:
    print('Connection Insert qa_ddldb_23_85')
    employee_id = str(65);
    salary_id = str(14)
    insert_query = 'insert into public.employee_salary(employee_id, salary_id) values(' + employee_id + ',' + salary_id +');'
    cursor.execute(insert_query);
    conn.commit();
    cursor.close();

