from flask import Blueprint


post_bp = Blueprint('user_post', __name__, url_prefix='/post')


# Получаем все посты

@post_bp.route('/', methods=['GET'])
def get_all_user_post():
    pass



# Получить определенный пост
@post_bp.route('/<int:post_id>/', methods=['GET'])
def get_exact_post(post_id: int, ):
    pass

# Изменить определенный пост
@post_bp.route('/<int:post_id>/<int:user_id>', methods=['PUT'])
def change_user_post(post_id: int, user_id: int):
    pass


# удаляем определенный пост
@post_bp.route('/<int:post_id>/<int:user_id>', methods=['DELETE'])
def delete_post(post_id: int, user_id: int):
    pass

# Публикация поста
@post_bp.route('/upload_post', methods=['GET'])
def create_post(post_text: str, post_photo: str, hashtags: list, user_id: int):
    pass

