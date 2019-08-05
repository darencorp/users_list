import datetime
import json
import unittest

from unittest.mock import patch

from app import app
from src.v1.users.tests.utils import UserAPIResponseMock


class TestUser(unittest.TestCase):

    def setUp(self):
        app.config['DEBUG'] = False
        app.testing = True
        self.client = app.test_client()

    @patch('src.v1.utils.requests.request')
    def test_should_get_single_user_instance(self, user_api_response):
        api_response = {
            'data': {
                'id': 1,
                'first_name': 'Test',
                'last_name': 'Test',
                'email': 'test@test.test',
                'avatar': 'http://test.test/test'
            }
        }

        user_api_response.return_value = UserAPIResponseMock(ok=True, text=json.dumps(api_response), status_code=200)

        expected = api_response['data']
        response = self.client.get('/v1/users/1', follow_redirects=True, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(json.loads(response.data), expected)

    @patch('src.v1.utils.requests.request')
    def test_should_get_user_list(self, user_api_response):
        api_response = {
            'data': [
                {
                    'id': 1,
                    'first_name': 'Test1',
                    'last_name': 'Test1',
                    'email': 'test@test.test',
                    'avatar': 'http://test.test/test'
                },
                {
                    'id': 2,
                    'first_name': 'Test2',
                    'last_name': 'Test2',
                    'email': 'test@test.test',
                    'avatar': 'http://test.test/test'
                },
                {
                    'id': 3,
                    'first_name': 'Test3',
                    'last_name': 'Test3',
                    'email': 'test@test.test',
                    'avatar': 'http://test.test/test'
                },
                {
                    'id': 4,
                    'first_name': 'Test4',
                    'last_name': 'Test4',
                    'email': 'test@test.test',
                    'avatar': 'http://test.test/test'
                },
                {
                    'id': 5,
                    'first_name': 'Test5',
                    'last_name': 'Test5',
                    'email': 'test@test.test',
                    'avatar': 'http://test.test/test'
                }
            ]
        }

        user_api_response.return_value = UserAPIResponseMock(ok=True, text=json.dumps(api_response), status_code=200)

        expected = api_response['data']
        response = self.client.get('/v1/users', follow_redirects=True, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertListEqual(json.loads(response.data), expected)

    @patch('src.v1.utils.requests.request')
    def test_should_get_user_list_from_second_page(self, user_api_response):
        api_response = {
            'data': [
                {
                    'id': 6,
                    'first_name': 'Test6',
                    'last_name': 'Test6',
                    'email': 'test@test.test',
                    'avatar': 'http://test.test/test'
                },
                {
                    'id': 7,
                    'first_name': 'Test7',
                    'last_name': 'Test7',
                    'email': 'test@test.test',
                    'avatar': 'http://test.test/test'
                },
                {
                    'id': 8,
                    'first_name': 'Test8',
                    'last_name': 'Test8',
                    'email': 'test@test.test',
                    'avatar': 'http://test.test/test'
                },
                {
                    'id': 9,
                    'first_name': 'Test9',
                    'last_name': 'Test9',
                    'email': 'test@test.test',
                    'avatar': 'http://test.test/test'
                },
                {
                    'id': 10,
                    'first_name': 'Test10',
                    'last_name': 'Test10',
                    'email': 'test@test.test',
                    'avatar': 'http://test.test/test'
                }
            ]
        }

        user_api_response.return_value = UserAPIResponseMock(ok=True, text=json.dumps(api_response), status_code=200)

        expected = api_response['data']
        response = self.client.get('/v1/users?page=2', follow_redirects=True, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertListEqual(json.loads(response.data), expected)

    @patch('src.v1.utils.requests.request')
    def test_should_create_user_instance(self, user_api_response):
        api_response = {
            'id': '1',
            'first_name': 'Test1',
            'last_name': 'Test1',
            'email': 'test@test.test',
            'avatar': 'http://test.test/test',
            'createdAt': datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        }

        user_api_response.return_value = UserAPIResponseMock(ok=True, text=json.dumps(api_response), status_code=201)

        data = {
            'first_name': 'Test1',
            'last_name': 'Test1',
            'email': 'test@test.test',
            'avatar': 'http://test.test/test'
        }

        response = self.client.post('/v1/users', follow_redirects=True, data=data, content_type='application/json')

        self.assertEqual(response.status_code, 201)
        self.assertDictEqual(json.loads(response.data), api_response)

    @patch('src.v1.utils.requests.request')
    def test_should_update_user_instance(self, user_api_response):
        api_response = {
            'id': '1',
            'first_name': 'Test2',
            'last_name': 'Test2',
            'email': 'test@test.test',
            'avatar': 'http://test.test/test',
            'updatedAt': datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        }

        user_api_response.return_value = UserAPIResponseMock(ok=True, text=json.dumps(api_response), status_code=200)

        data = {
            'first_name': 'Test2',
            'last_name': 'Test2',
            'email': 'test@test.test',
            'avatar': 'http://test.test/test'
        }

        response = self.client.put('/v1/users/1', follow_redirects=True, data=data, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(json.loads(response.data), api_response)

    @patch('src.v1.utils.requests.request')
    def test_should_delete_user_instance(self, user_api_response):
        user_api_response.return_value = UserAPIResponseMock(ok=True, text='', status_code=204)

        response = self.client.delete('/v1/users/1', follow_redirects=True)

        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.data, b'')

    @patch('src.v1.utils.requests.request')
    def test_should_return_error_description_if_timeout(self, user_api_response):
        user_api_response.return_value = None

        response = self.client.get('/v1/users/1', follow_redirects=True)

        self.assertEqual(response.status_code, 503)
        self.assertEqual(response.data.decode(), '"External API is unavailable!"')

    @patch('src.v1.utils.requests.request')
    def test_should_return_error_description_if_instance_not_found(self, user_api_response):
        user_api_response.return_value = UserAPIResponseMock(ok=False, reason='Not Found', status_code=404)

        response = self.client.get('/v1/users/1', follow_redirects=True)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data.decode(), '"Not Found"')
