from src.utils import NestableBlueprint
from .views.user import UserView

users_blueprint = NestableBlueprint('users', __name__)
users_blueprint.register_view(UserView.as_view('users'), '/', pk='user_id')
