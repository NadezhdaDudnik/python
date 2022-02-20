def user_info(email, user_emails, users_storage):
    message = ''
    if email in user_emails:
        message = 'User_email=', email, 'User_info:', users_storage[email]
        return message
    else:
        message = 'No user with email: ', email
        return message


def all_users_info(users_storage):
    for k, y in users_storage.items():
        user_email = "User_email: " + k
        user_info_1 = 'User_info', y

        print(user_email,  user_info_1)
