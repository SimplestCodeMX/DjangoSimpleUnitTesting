from django.utils.translation import gettext as _
from django.utils.text import slugify
from django.utils.html import mark_safe
from django.conf import settings
from django.urls import reverse_lazy
from django.core.files.images import get_image_dimensions

import requests


class Utils:

    def __init__(self):
        pass

    @classmethod
    def get_unique_slug(cls, model_instance, slugable_field_name, slug_field_name):
        """
        Takes a model instance, sluggable field name (such as 'title') of that
        model as string, slug field name (such as 'slug') of the model as string;
        returns a unique slug as string.
        """
        slug = slugify(getattr(model_instance, slugable_field_name))
        unique_slug = slug
        extension = 1
        ModelClass = model_instance.__class__

        while ModelClass._default_manager.filter(
                **{slug_field_name: unique_slug}
        ).exists():
            unique_slug = f'{slug}-{extension}'
            extension += 1

        return unique_slug

    @classmethod
    def image_size_is_valid(cls, request_data, def_width, def_height, image_field):
        if request_data.get(image_field):
            image = request_data.get(image_field)
            width, height = get_image_dimensions(image)
            if width >= def_width and height >= def_height:
                return True
        return True

    @classmethod
    def count_filter_result(cls, model_class, query_filter, is_staff=False):
        if query_filter:
            return model_class.objects.filter(**query_filter).count()
        if is_staff:
            return model_class.objects.all().count()
        return 0

    @classmethod
    def filter_result(cls, model_class, query_filter):
        if query_filter:
            return model_class.objects.filter(**query_filter)
        return []

    @classmethod
    def get_value_list_field_from_filter(cls, model_class, field, query_filter):
        if hasattr(model_class, field) and query_filter:
            return model_class.objects.values_list('id', flat=True).filter(**query_filter)
        return []
