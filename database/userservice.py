from models import User, Password, db

# Регистрация пользователя
def register_user_db(**user_data):
    new_user = User(**user_data)


    db.session.add(new_user)
    db.session.commit()


# Проверка пользователя
def check_user_db(email):
    pass


#проверка пароля
def check_user_password_db(email, password):
    pass


# Получение всех пользователей с базы
def get_all_users_db():
    pass

# Получить конкретного пользователя
def get_exact_user_db(user_id):
    pass

# Удалить пользователя из базы
def delete_user_db(user_id):
    pass