from flask import Blueprint


comment_bp = Blueprint('comment', __name__, url_prefix='/comment')


# Получаем комментарии определенного пользователя

@comment_bp.route('/<int:post_id>', methods=['GET'])
def get_exact_post_comment(post_id: int):
    pass



# Публикация комментария
@comment_bp.route('/<int:post_id>/<int:comment_user_id>', methods=['GET'])
def get_exact_user(post_id: int, comment_user_id: int):
    pass

# Изменить данные пользователя по user_id
@comment_bp.route('/<int:comment_id>/<int:comment_user_id>', methods=['POST'])
def publisher_comment(comment_id: int, comment_user_id: int):
    pass


# Изменить опубликованный комментарий
@comment_bp.route('/<int:comment_user_id>/<int:comment_id>', methods=['PUT'])
def change_comment(comment_user_id: int, comment_id: int):
    pass

# удаляем комментарий
@comment_bp.route('/<int:comment_user_id>', methods=['DELETE'])
def delete_comment(comment_user_id: int):
    pass

