from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_user, name='loginurl'),
    path('logout', views.logout_user, name='logouturl'),
    path('register', views.register_user, name='registerurl'),
    path('about', views.about, name='abouturl'),
]
