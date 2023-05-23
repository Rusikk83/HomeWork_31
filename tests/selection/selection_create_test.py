import pytest

from tests.factories import AdFactory


@pytest.mark.django_db
def test_selection_create(client, user_with_access_token):
    user, access_token = user_with_access_token
    ad_list = AdFactory.create_batch(4)
    data = {
        "name": "Test",
        "item": [ad.pk for ad in ad_list]
    }

    expected_data = {
        "id": 1,
        "owner": user.username,
        "name": "Test",
        "item": [ad.pk for ad in ad_list]
        }
    response = client.post(f"/selection/", data=data, HTTP_AUTHORIZATION=f'Bearer {access_token}')
    assert response.status_code == 201
    assert response.data == expected_data
