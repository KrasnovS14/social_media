from flask_sqlalchemy import SQLAlchemy


# Создаем обьекты базу данных

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    username = db.Column(db.String, nullable = False)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, nullable = False)
    birthday = db.Column(db.Date, nullable = False)
    register_date = db.Column(db.DateTime)


# Таблица паролей
class Password(db.Model):
    __tablename__ = 'user_password'
    user_id= db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    password = db.Column(db.String, nullable = False)



#  Таблица фотографий
class PostPhoto(db.Model):
    __tablename__ = 'user_photo'
    photo_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable = False)
    photo_path = db.Column(db.String, nullable = False)




# Таблица постов
class Post(db.Model):
    __tablename__ = 'user_post'
    post_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    photo_id = db.Column(db.Integer, db.ForeignKey('users_photo.photo_id'), nullable=False)
    post_text = db.Column(db.String, nullable=False)
    post_date = db.Column(db.DateTime)

    user_fk = db.relationship(User)
    photo_fk = db.relationship(PostPhoto)


# Таблица для комментариев
class PostComment(db.Model):
    __tablename__ = 'post_comment'
    comment_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    post_id = db.Column(db.Integer, db.ForeignKey('users_post.post_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    comment_text = db.Column(db.String, nullable=False)
    comment_date = db.Column(db.DateTime)

    user_fk = db.relationship(User)
    post_fk = db.relationship(Post)

# Таблица хэштегов

class HashTag(db.Model):
    __tablename__ = 'hashtags'
    hashtag_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    post_id = db.Column(db.Integer, db.ForeignKey('users_post.post_id'), nullable=False)
    hashtag_name = db.Column(db.String, nullable=False)

    post_fk = db.relationship(Post)