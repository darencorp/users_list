from src.v1.utils import fetch_api_data
from src.v1.config import USERS_PER_PAGE


class UserAPIFacade:

    def list(self, page):
        response, status = fetch_api_data('GET', f'/users?page={page}&per_page={USERS_PER_PAGE}')

        response = response['error'] if response.get('error') else response['data']
        return response, status

    def retrieve(self, user_id):
        response, status = fetch_api_data('GET', f'/users/{user_id}')

        response = response['error'] if response.get('error') else response['data']
        return response, status

    def create(self, data):
        headers = {'Content-Type': 'application/json'}
        response, status = fetch_api_data('POST', '/users', data=data, headers=headers)

        response = response if response.get('error') else response
        return response, status

    def update(self, user_id):
        headers = {'Content-Type': 'application/json'}
        response, status = fetch_api_data('PUT', f'/users/{user_id}', headers=headers)

        response = response if response.get('error') else response
        return response, status

    def delete(self, user_id):
        response, status = fetch_api_data('DELETE', f'/users/{user_id}')

        response = response if response and response.get('error') else response
        return response, status
