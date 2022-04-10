from django.urls import path

from . import consumer

websocket_urlpatterns = [
	path('ws/room/<str:roomId>/',consumer.RoomConsumer.as_asgi())
]