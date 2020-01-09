from django.urls import path
from books import views

urlpatterns = [
path('books/', views.User_list),
path('books/<int:pk>/',
views.User_detail),]