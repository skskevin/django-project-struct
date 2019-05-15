#!/usr/bin/env python
# -*- coding: utf-8 -*-
from holydog.settings.base import *

DEBUG = True
# ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'NAME': 'holydog',
        'USER': 'root',
        'PASSWORD': '',
    }
}

# CACHE CONFIG
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# DJANGO DEBUG TOOLBAR
# MIDDLEWARE_CLASSES += (
#    'debug_toolbar.middleware.DebugToolbarMiddleware',
# )

# INSTALLED_APPS += (
#    'debug_toolbar',
# )

# EMAIL CONFIGURATION
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
