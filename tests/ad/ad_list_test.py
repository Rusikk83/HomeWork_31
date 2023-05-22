from operator import itemgetter
import json

import pytest

from tests.factories import AdFactory


@pytest.mark.django_db
def test_ad_list(client):
    ad_list = AdFactory.create_batch(4)
    response = client.get(f"/ad/")
    assert response.status_code == 200

    list = []

    # сериализация созданных записей
    for ad in ad_list:
        list.append({
            "id": ad.id,
            "name": ad.name,
            "author_id": ad.author_id,
            "price": ad.price,
            "description": ad.description,
            "category_id": ad.category_id,
            "is_published": ad.is_published,
            "image": ad.image.url if ad.image else None,
        })
    list_sort = sorted(list, key=itemgetter('name'))  # сортировка по имени, как и во вьюсете
    result = {
        'items': list_sort,
        'num_pages': 1,
        'total': 4,

    }
    result_response = dict(json.loads(response.content))

    assert result_response == result

