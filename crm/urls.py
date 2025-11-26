from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_user, name='loginurl'),
    path('logout', views.logout_user, name='logouturl'),
    path('register', views.register_user, name='registerurl'),
    path('record/<int:pk>' , views.record_detail, name='record_detail'),
    path('delete_record/<int:pk>' , views.delete_record, name='delete_record'),
    path('add_record', views.add_record, name='add_record'),
    path('about', views.about, name='abouturl'),
]
