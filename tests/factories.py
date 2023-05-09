import factory.django

from ads.models import User, Categories, Ads


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")



class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Categories

    name = factory.Faker("name")
    slug = factory.Faker("ean", length=8)


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ads

    name = factory.Faker("name")
    price = 110
    category = factory.SubFactory(CategoryFactory)
    author = factory.SubFactory(UserFactory)