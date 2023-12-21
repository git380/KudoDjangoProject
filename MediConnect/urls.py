from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('welcome/', views.welcome, name='welcome'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('hospital_list/', views.hospital_list, name='hospital_list'),
    path('tel_change/', views.tel_change, name='tel_change'),
    path('hospital_search/', views.hospital_search, name='hospital_search'),
    path('pw_change/', views.pw_change, name='pw_change'),
    path('patient_registration/', views.patient_registration, name='patient_registration'),
]
