from django.urls import path
from books import views


app_name = 'books'
urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('users/', views.User_list.as_view(), name="users"),
    path('user_detail/<int:pk>/', views.User_detail.as_view(), name="user_detail"),
    path('public_chats/', views.PublicChatRoom_list.as_view(), name="public_chats"),
    path('public_detail/<int:pk>/', views.PublicChatRoom_detail.as_view(), name="public_detail"),
    path('private_chats/', views.PrivateChatRoom_list.as_view(), name="private_chats"),
    path('private_detail/<int:pk>/', views.PrivateChatRoom_detail.as_view(), name="private_detail"),
    path('ban_list/', views.ChatBan_list.as_view(), name="ban_list"),
    path('ban_detail/<int:pk>/', views.ChatBan_detail.as_view(), name="ban_detail"),
    path('block_list/', views.UserBlock_list.as_view(), name="block_list"),
    path('block_detail/<int:pk>/', views.UserBlock_detail.as_view(), name="block_detail"),
    path('chatUser_list/', views.ChatRoomUser_list.as_view(), name="chatUser_list"),
    path('chatUser_detail/<int:pk>/', views.ChatRoomUser_detail.as_view(), name="chatUser_detail"),
    path('admin_list/', views.ChatAdmin_list.as_view(), name="admin_list"),
    path('admin_detail/<int:pk>/', views.ChatAdmin_detail.as_view(), name="admin_detail"),

]