import json

from flask import Response, request
from flask.views import MethodView

from src.v1.users.facades.user_api import UserAPIFacade


class UserView(MethodView):

    user_api = UserAPIFacade()

    def post(self):
        new_user, status = self.user_api.create({})
        return Response(json.dumps(new_user), status)

    def get(self, user_id):
        if user_id:
            user_instance, status = self.user_api.retrieve(user_id)
            return Response(json.dumps(user_instance), status)

        page = request.args.get('page', 1)

        user_list, status = self.user_api.list(page)
        return Response(json.dumps(user_list), status)

    def delete(self, user_id):
        data, status = self.user_api.delete(user_id)
        return Response(json.dumps(data), status)

    def put(self, user_id):
        updated_user, status = self.user_api.update(user_id)
        return Response(json.dumps(updated_user), status)
