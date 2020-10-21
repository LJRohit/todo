from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list'),
    path('update_task/<str:pkey>/', views.updateTask, name='update_task'),
    path('delete/<str:pkey>/', views.deleteTask, name='delete'), 
]
