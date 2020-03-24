from flask import Blueprint

bp = Blueprint('alert', __name__, url_prefix='/alert')


@bp.route('', methods=['GET'])
def log_alert():
    print('Alert logged, someone launched a Bash shell...')
    return 'OK', 200