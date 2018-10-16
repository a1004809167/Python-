from django.urls import path
from . import views

urlpatterns = [
    path('insert', views.insert, name='insert'),
    path('update', views.update, name='update'),
    path('search', views.search, name='search'),
    path('delete', views.delete, name='delete'),
    path('create', views.create, name='create'),
    path('create_post', views.create_post, name='create_post'),
    path('delete_post', views.delete_post, name='delete_post'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('register_in', views.register_in, name='register_in'),
    path('logout', views.logout, name='logout'),
]
