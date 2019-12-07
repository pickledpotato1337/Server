from django.shortcuts import render
from .models import User, PublicChatRoom, PrivateChatRoom, ChatBan, UserBlock, ChatRoomUser, ChatAdmin
from .serializers import UserSerializer, PublicChatRoomSerializer, PrivateChatRoomSerializer, ChatBanSerializer,  UserBlockSerializer, ChatRoomUserSerializer, ChatAdminSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser



def User_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def PublicChatRoom_list(request):

    if request.method == 'GET':
        publicChatRoom = PublicChatRoom.objects.all()
        serializer = PublicChatRoomSerializer(publicChatRoom, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PublicChatRoomSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def PrivateChatRoom_list(request):
    if request.method == 'GET':
        privateChatRoom = PrivateChatRoom.objects.all()
        serializer = PrivateChatRoomSerializer(privateChatRoom, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PrivateChatRoomSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def ChatBan_list(request):
    if request.method == 'GET':
        chatBan = ChatBan.objects.all()
        serializer = ChatBanSerializer(chatBan, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PrivateChatRoomSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)