


import pytest

@pytest.fixture()
@pytest.mark.django_db
def access_token(client, django_user_model):
    username = "test_user"
    password = "qwerty"
    age = 21
    role = 'moderator'
    location_id = 7

    django_user_model.objects.create(username=username, password=password, role=role, age=age, location_id=location_id)
    response = client.post("user/token/", {"username": username, "password": password})
    return response.data.get("access_token")

