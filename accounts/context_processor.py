from django.conf import settings


def get_logged_user(request):
    data = {
        'username': '',
        'full_name': '',
        'selfie': '',
        'role': '',
        'email': ''
    }
    return {"logged_user": data}
