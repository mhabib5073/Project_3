from django.urls import path
from testApp import views


urlpatterns = [
    path('',views.home, name='home' ),
    path('create/', views.create, name='create'),
    path('edit/<int:pk>/', views.update, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),

]