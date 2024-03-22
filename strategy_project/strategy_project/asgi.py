"""
ASGI config for strategy_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'strategy_project.settings')

# application = get_asgi_application()
django_asgi_app = get_asgi_application()

from channels.routing import ProtocolTypeRouter

from channels.routing import URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
# import chat.routing
from new_chat import routing

application = ProtocolTypeRouter({
  'http': django_asgi_app,
  'websocket': AllowedHostsOriginValidator(AuthMiddlewareStack( URLRouter( routing.websocket_urlpatterns ) )),
})