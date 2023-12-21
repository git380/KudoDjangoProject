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
    path('patient_all/', views.patient_all, name='patient_all'),
    path('patient_update/', views.patient_update, name='patient_update'),
    path('patient_search_by_name/', views.patient_search_by_name, name='patient_search_by_name'),
    path('patient_search/', views.patient_search, name='patient_search'),
    path('treatment_selection/', views.treatment_selection, name='treatment_selection'),
    path('treatment_delete/', views.treatment_delete, name='treatment_delete'),
    path('treatment_confirmation/', views.treatment_confirmation, name='treatment_confirmation'),
]
