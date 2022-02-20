from create import create_user
from read import user_info, all_users_info

user_emails = []
users_storage = {}

while True:
    action = input("Please enter create or read or update or delete \n")
    if action == 'create':
        print('action = ', action)
        #if email ==
        email = input('Enter email: \n')
        name = input('Enter name: \n')
        password = input('Enter password: \n')
        phone = input('Enter phone: \n')

        create_user(email, name, password, phone, user_emails, users_storage)
        print("user_emails", user_emails)
        print("user_storage", users_storage)

    elif action == 'read_all':
        print('action = ', action)
        all_users_info(users_storage)
    elif action == 'read_user':
        print('action = ', action)
        user_e = input('Enter user_email: \n')
        message = user_info(user_e, user_emails, users_storage)

        print('User = ', message)
    elif action == 'update':
        print('action = ', action)
    elif action == 'delete':
        print('action = ', action)
    else:
        print('Please enter create or read or update or delete')