
class AdminMixins(object):

    @staticmethod
    def display_image(obj, model_field='cover_image'):
        if hasattr(obj, model_field):
            image_obj = getattr(obj, model_field)
            slug = getattr(obj, 'slug') if hasattr(obj, 'slug') else '-'
            return mark_safe(
                f'<img src="{image_obj.url}" alt="{slug}" style="width:300px; height: 120px;">'
            )

        return mark_safe(
            f"<p>{_('File not found')}</p>"
        )

    @staticmethod
    def display_asset(obj, model_field='asset'):
        if hasattr(obj, model_field):
            image_obj = getattr(obj, model_field)
            slug = getattr(obj, 'slug') if hasattr(obj, 'slug') else '-'
            return mark_safe(
                f'<img src="{image_obj.url}" alt="{slug}" style="width:300px; height: 120px;">'
            )

        return mark_safe(
            f"<p>{_('File not found')}</p>"
        )