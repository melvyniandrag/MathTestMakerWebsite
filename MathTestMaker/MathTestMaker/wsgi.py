"""
WSGI config for MathTestMaker project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

import sys # To do verify me

from django.core.wsgi import get_wsgi_application

sys.path.append('/home/mathtestmakeruser/MathTestMakerLibrary/mathtestmaker') # TODO verify me
sys.path.append('/home/mathtestmakeruser/MathTestMakerWebsite/MathTestMaker') # TODO verify me
sys.path.append('/home/mathtestmakeruser/MathTestMakerWebsite') # TODO verify me
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MathTestMaker.settings')

application = get_wsgi_application()
