from django.urls import path
from . import views

app_name = 'gift'
urlpatterns = [
    path('home', views.index, name="index"),
    path('registration', views.registration, name="registration"),
    path('login', views.login, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('create', views.create, name="create"),
]