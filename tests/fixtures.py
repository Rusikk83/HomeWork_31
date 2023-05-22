


import pytest

@pytest.fixture()
@pytest.mark.django_db
def access_token(client, django_user_model):
    username = "test_user"
    password = "qwerty"
    age = 21
    role = 'moderator'
    user = django_user_model.objects.create(username=username, password=password)
    user.set_password(user.password)
    user.save()
    log = client.login(username=username, password=password)
    #resp = client.post("/user/create/", {"username": "Test_password_1", "password": "qwerty"})
    response = client.post("/user/token/", data={"username": username, "password": password})
    return response.data.get("access")

