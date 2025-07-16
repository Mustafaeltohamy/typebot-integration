from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Authentication URLs
    path('login/', views.custom_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
    # Bot Management URLs
    path('bots/', views.bot_list, name='bot_list'),
    path('bots/<str:bot_id>/embed/', views.embed_bot, name='embed_bot'),
    
    # Analytics URL
    path('analytics/', views.analytics, name='analytics'),
    
    # Webhook URL
    path('webhook/typebot/', views.typebot_webhook, name='typebot_webhook'),
    
    # Home redirect
    path('', views.custom_login, name='home'),
]