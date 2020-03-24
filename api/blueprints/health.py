from flask import Blueprint

bp = Blueprint('health', __name__, url_prefix='/health')


@bp.route('', methods=['GET'])
def get_health():
    print('Health check hit...')
    return 'OK', 200