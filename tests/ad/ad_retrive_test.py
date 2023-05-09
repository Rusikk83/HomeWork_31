import pytest

from ads.serializers.ad_serialize import AdsDetailSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_ad_retrieve(client, access_token):
    ad = AdFactory.create()
    response = client.get(f"/ad/{ad.pk}/")
    assert response.stutus_code == 200
    assert response.data == AdsDetailSerializer(ad)
