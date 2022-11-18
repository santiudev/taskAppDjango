from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.getTask),
    path('post/', views.postTask),
    path('put/<int:pk>/', views.putTask),
    path('delete/<int:pk>/', views.deleteTask)
]