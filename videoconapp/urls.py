from django.urls import path
from . import views

urlpatterns = [
    path('',views.user_register),
    path('login',views.login_view),
    path('dashboard',views.dashboard),
    # path('video-conferencing/', views.video_conferencing),
    path('meeting',views.videocall),
    path('joinroom',views.join_room),
    path('logout',views.user_logout),
]
