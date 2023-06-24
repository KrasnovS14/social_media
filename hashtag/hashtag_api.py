from flask import Blueprint


hashtag_bp = Blueprint('hashtag', __name__, url_prefix='/hashtag')


# Получить хэштег по количеству
@hashtag_bp.route('/', methods= ['GET'])
def get_hashtags(size: int):
    pass

# Получить определенный хэштег
@hashtag_bp.route('/string: hashtag_name', methods= ['GET'])
def get_exact_hashtags(hashtag_name: str):
    pass


