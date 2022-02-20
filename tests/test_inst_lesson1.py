import pytest
import requests
import jsonmodels
from tests.service.petstore import PetStore


def test_post_pet():
    json_data = {
        "id": 12,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "dog",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

    response = PetStore().post_pet(json_data)
    print(response.status_code)
    print(response.json())
