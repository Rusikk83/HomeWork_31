import pytest

from ads.serializers.ad_serialize import AdsDetailSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_ad_create(client, user, categories, access_token):
    data = {
        "author": user.username,
        "category": categories.name,
        "name": 'Тестовое имя',
        "price": 12121212
    }
    response = client.post(f"/ad/create/", data=data, HTTP_AUTHORIZATION=f'Bearer {access_token}')
    assert response.status_code == 201
    # assert response.data == AdsDetailSerializer(ad).data
