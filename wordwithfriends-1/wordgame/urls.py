from django.urls import path
from . import views

urlpatterns = [
	path('login/',views.login_page, name='login'),
	path('logout/',views.logout_user, name='logout'),
	path('signup/',views.signup_user, name='signup'),
	path('', views.home_page, name='home'),
	path('room/<str:roomId>/', views.room_page, name='room'),
	path('room_info/<str:roomId>/', views.get_room_info, name='room_info'),
	path('user/<str:username>/', views.user_page, name='user'),
	path('create_room/', views.create_room, name='create_room'),
	path('giveup/<str:roomId>/', views.giveup, name='giveup'),
	path('rooms/', views.available_rooms, name='rooms'),
	path('leaderboards/', views.get_leaderboards, name='leaderboards'),
]
