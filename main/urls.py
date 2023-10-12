from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('barbers/', views.barber_list, name='barber_list'),
    path('barbers/<int:pk>/', views.barber_detail, name='barber_detail'),
    path('services/', views.service_list, name='service_list'),
    path('services/<int:pk>/', views.service_detail, name='service_detail'),
    path('register/', views.register, name='register'),
]
