# -*- coding: utf-8 -*-

from .base import *

DEBUG = True

"""
***********************
*   Force SSL/HTTPS   *
***********************
"""

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'http')

"""
********************************
* PRODUCTION MIDDLEWARE ADDITION *
********************************
"""

MIDDLEWARE += [

]

"""
*******************
* DATABASE CONFIG *
*******************
"""

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'training_unit_test',
        'USER': 'apps_server',
        'PASSWORD': '2018apps',
        'HOST': 'localhost',
        'PORT': '',
    }
}

"""
*************************
* DEVELOP APPS ADDITION *
*************************
"""

INSTALLED_APPS += [
    'gunicorn',
]

"""
###############################
# TEMPLATES ADDITION SETTINGS #
###############################
"""

TEMPLATES[0]['OPTIONS']['context_processors'] += [

]

"""
#################
# SYSTEM CONFIG #
#################
"""

SITE_URL = 'https://localhost:8100'
SENDING_EMAILS_ENABLED = True


"""
###################
# Logger Tracking #
###################
"""

# sentry_sdk.init(
#     dsn="https://326ef95239a2446b99c542cdfca7a5b4@o213835.ingest.sentry.io/5530095",
#     integrations=[DjangoIntegration()],
#     traces_sample_rate=1.0,
#     # If you wish to associate users to errors (assuming you are using
#     # django.contrib.auth) you may enable sending PII data.
#     send_default_pii=True
# )