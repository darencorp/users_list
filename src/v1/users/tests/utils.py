import json


class UserAPIResponseMock:

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def json(self):
        return json.loads(self.text)
