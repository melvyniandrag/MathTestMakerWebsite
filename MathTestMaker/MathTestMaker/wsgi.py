"""
WSGI config for MathTestMaker project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

import sys # To do verify me

from django.core.wsgi import get_wsgi_application

sys.path.append('/MathTestMakerLibrary/mathtestmaker') # TODO verify me
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MathTestMaker.settings')

application = get_wsgi_application()
