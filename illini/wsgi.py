"""
WSGI config for illini project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(os.path.join(BASE_DIR, 'venv/lib/python3.4/site-packages'))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "illini.settings")

application = get_wsgi_application()
