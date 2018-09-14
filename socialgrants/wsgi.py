"""
WSGI config for socialgrants project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

# sys.path.append('/home/raju/Documents/socialjoy-env/lib/python3.6')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socialgrants.settings')

application = get_wsgi_application()
