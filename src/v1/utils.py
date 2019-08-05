import requests
from requests import RequestException

from .config import USER_API_URL


def fetch_api_data(method, url, **kwargs):
    try:
        response = requests.request(method, f'{USER_API_URL}{url}', **kwargs)
    except RequestException:
        return {'error': 'External API is unavailable!'}, 503

    if not response:
        return {'error': 'External API is unavailable!'}, 503

    if not response.ok:
        return {'error': response.reason}, response.status_code

    return response.json() if response.text else '', response.status_code
