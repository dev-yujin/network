"""mProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'mafia'
urlpatterns = [
    path('reg/', views.register, name='reg'),
	path('regCon/', views.regConMafia, name='regCon'),
	path('room/', views.waitingRoom, name='room'),
    path('game/', views.game, name='game'),
    path('polls/', views.polls, name='polls'),
    path('vic_mafia/', views.vic_mafia, name='vic_mafia'),
    path('vic_citizen/', views.vic_citizen, name='vic_citizen'),
    path('', views.index, name='index'),
    path('<str:room_name>/', views.chat, name='chat'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
