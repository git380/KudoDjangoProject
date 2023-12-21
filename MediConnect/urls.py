from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('welcome/', views.welcome, name='welcome'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('hospital_list/', views.hospital_list, name='hospital_list'),
]
