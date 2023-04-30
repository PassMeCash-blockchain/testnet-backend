import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter,get_default_application
from django.core.asgi import get_asgi_application
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path,re_path

from websockets.consumers import WebsocketCluster



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    'websocket':AllowedHostsOriginValidator(
    AuthMiddlewareStack(
        URLRouter([
            path('ws/cluster/<str:layer_id>/', WebsocketCluster.as_asgi())
        ])
   )
   )
}
)
