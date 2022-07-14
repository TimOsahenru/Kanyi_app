from django.urls import path
from . import views


urlpatterns = [
    path('login', views.customlogin, name='login'),
    path('logout', views.customlogout, name='logout'),
    path('register', views.register, name='register'),
    path('taskcreate', views.taskcreate, name='taskcreate'),
    path('taskdelete/<int:pk>/', views.taskdelete, name='taskdelete'),
    path('taskedit/<int:pk>/', views.taskedit, name='taskedit'),
    path('taskdetail/<int:pk>/', views.taskdetail, name='taskdetail'),
    path('', views.tasklist, name='tasklist'),
]
