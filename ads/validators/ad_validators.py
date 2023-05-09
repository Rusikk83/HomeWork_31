from rest_framework.exceptions import ValidationError


def check_is_published(value):
    if value:
        raise ValidationError("Нельзя создавать опубликованные объявления")
