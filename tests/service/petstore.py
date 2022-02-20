import json

import requests
import jsonmodels


def logger(fn):
    def wrap(*args, **kwargs):
        print(fn.__name__)
        res = fn(*args, **kwargs)
        print(res)
        try:
            print(res.json())
        except json.JSONDecodeError:
            ...
        return res

    return wrap


class PetStore:
    def __init__(self, url=None, headers=None):
        self.url = url or 'https://petstore.swagger.io'
        self.headers = headers
        self.session = requests.Session()
        self.session.headers = self.headers

    @logger
    def post_pet(self, json):
        response = self.session.post(url=f'{self.url}/v2/pet', json=json)
        return response

    #правила для pytest
# if name_of_file == (test_*.py OR *_test.py)
#     if def_name_outOfClass == "test" + def_name
#     if class_name == "Test" + className
#         if def_name_InClass == "test" + def_name

#запуска автотеста на pytest
#pytest -v test_lesson_3_2_step13.py