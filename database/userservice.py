from database.models import User, Password, db

#Регистрация
def register_user_db(**user_data):
    new_user = User(**user_data)
    db.session.add(new_user)
    db.session.commit()

#Проверка пользователя по почте
def check_user_db(email):
    checker_email = User.query.filter_by(email=email).first()
    if checker_email:
        return True
    return False

#Проверка пароля пользователя
def check_user_password_db(email, password):
    checker_email = User.query.filter_by(email=email).first()
    checker_pass = Password.query.filter_by(password=password).first()
    if checker_email and checker_pass:
        return True
    return False

#Получить всех пользователей из базы
def get_all_users_db():
    users = User.query.all()
    return users

#Получить определенного пользователя
def get_exact_user_db(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    return user

#Удалить пользователя из базы
def delete_user_db(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    else:
        return False