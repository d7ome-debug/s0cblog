"""
WSGI config for socblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.utils.translation import gettext_lazy as _
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socblog.settings')

application = get_wsgi_application()

app = application # add this line.