from flask import Blueprint, request


photo_bp = Blueprint('photo', __name__, url_prefix='/photo')


# Получаем фото всех пользователей

@photo_bp.route('/', methods=['GET'])
def get_all_photo():
    pass

# Публикация фото
@photo_bp.route('/', methods=['POST'])
def publish_photo():
    # Получить фото из фронт части
    files = request.files.get('image', '')
    files.save = ('user_images/'+ files.filename)
    print(files)
    return 'Hello'

# Получить фото определенного  пользователя по photo_id

@photo_bp.route('/<int:user_id>', methods=['GET'])
def get_exact_user_photo(user_id: int):
    pass
# Получить определенное фото пользователя
@photo_bp.route('/<int:photo_id>', methods=['GET'])
def get_exact_photo(photo_id: int):
    pass

# Изменить данные пользователя по photo_id
@photo_bp.route('/<int:user_id>/<int:photo_id>', methods=['PUT'])
def change_user_photo(photo_id: int, user_id: int):
    pass


# удалить фото пользователя

@photo_bp.route('/<int:user_id>/<int:photo_id>', methods=['DELETE'])
def delete_user_photo(photo_id: int):
    pass

