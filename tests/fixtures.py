


import pytest

@pytest.fixture()
@pytest.mark.django_db
def access_token(client, django_user_model):
    username = "test_user"
    password = "qwerty"

    user = django_user_model.objects.create(username=username, password=password)
    user.set_password(user.password)
    user.save()
    log = client.login(username=username, password=password)

    response = client.post("/user/token/", data={"username": username, "password": password})
    return response.data.get("access")

@pytest.fixture()
@pytest.mark.django_db
def user_with_access_token(client, django_user_model):
    username = "test_user"
    password = "qwerty"

    new_user = django_user_model.objects.create(username=username, password=password)
    new_user.set_password(new_user.password)
    new_user.save()
    log = client.login(username=username, password=password)

    response = client.post("/user/token/", data={"username": username, "password": password})
    return new_user, response.data.get("access")
