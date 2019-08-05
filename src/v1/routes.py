from src.utils import NestableBlueprint
from .users.routes import users_blueprint

api_v1 = NestableBlueprint('v1', __name__)

api_v1.register_blueprint(users_blueprint, url_prefix='/users')
