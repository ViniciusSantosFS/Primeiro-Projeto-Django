#a aplicação começa nesse arquivo, é ele quem anda para o nosso settings

"""
WSGI config for meuPrimeiroProjeto project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meuPrimeiroProjeto.settings')

application = get_wsgi_application()
