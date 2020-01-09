from django.shortcuts import render
from .models import User, PublicChatRoom, PrivateChatRoom, ChatBan, UserBlock, ChatRoomUser, ChatAdmin
from .serializers import UserSerializer, PublicChatRoomSerializer, PrivateChatRoomSerializer, ChatBanSerializer,  UserBlockSerializer, ChatRoomUserSerializer, ChatAdminSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status


def User_list(request):

    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def User_detail(request, pk, format=None):

    try:
        question = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(question)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        serializer = UserSerializer(question)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        question.delete()
    return JsonResponse(status=status.HTTP_204_NO_CONTENT)


def PublicChatRoom_list(request):


    if request.method == 'GET':
        publicChatRoom = PublicChatRoom.objects.all()
        serializer = PublicChatRoomSerializer(publicChatRoom, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PublicChatRoomSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def PublicChatRoom_detail(request, pk, format=None):

    try:
        question = PublicChatRoom.objects.get(pk=pk)
    except PublicChatRoom.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = PublicChatRoomSerializer(question)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':

        serializer = PublicChatRoomSerializer(question)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        question.delete()
    return JsonResponse(status=status.HTTP_204_NO_CONTENT)


def PrivateChatRoom_list(request):

    if request.method == 'GET':
        privateChatRoom = PrivateChatRoom.objects.all()
        serializer = PrivateChatRoomSerializer(privateChatRoom, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PrivateChatRoomSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def PrivateChatRoom_detail(request, pk, format=None):

    try:
        question = PrivateChatRoom.objects.get(pk=pk)
    except PrivateChatRoom.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PrivateChatRoomSerializer(question)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':

        serializer = PrivateChatRoomSerializer(question)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        question.delete()
    return JsonResponse(status=status.HTTP_204_NO_CONTENT)


def ChatBan_list(request):

    if request.method == 'GET':
        chatBan = ChatBan.objects.all()
        serializer = ChatBanSerializer(chatBan, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ChatBanSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def ChatBan_detail(request, pk, format=None):

    try:
        question = ChatBan.objects.get(pk=pk)
    except ChatBan.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = ChatBanSerializer(question)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':

        serializer = ChatBanSerializer(question)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        question.delete()
    return JsonResponse(status=status.HTTP_204_NO_CONTENT)


def UserBlock_list(request):

    if request.method == 'GET':
        userBlock = UserBlock.objects.all()
        serializer = UserBlockSerializer(userBlock, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserBlockSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def UserBlock_detail(request, pk, format=None):
    try:
        question = UserBlock.objects.get(pk=pk)
    except UserBlock.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = UserBlockSerializer(question)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        serializer = UserBlockSerializer(question)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        question.delete()
    return JsonResponse(status=status.HTTP_204_NO_CONTENT)


def ChatRoomUser_list(request):

    if request.method == 'GET':
        chatRoomUser = ChatRoomUser.objects.all()
        serializer = ChatRoomUserSerializer(chatRoomUser, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ChatRoomUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def ChatRoomUser_detail(request, pk, format=None):

    try:
        question = ChatRoomUser.objects.get(pk=pk)
    except ChatRoomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = ChatRoomUserSerializer(question)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        serializer = ChatRoomUserSerializer(question)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        question.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)


def ChatAdmin_list(request):

    if request.method == 'GET':
        admin = ChatAdmin.objects.all()
        serializer = ChatAdminSerializer(admin, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ChatAdminSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def ChatAdmin_detail(request, pk, format=None):

    try:
        question = ChatAdmin.objects.get(pk=pk)
    except ChatAdmin.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = ChatAdminSerializer(question)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':

        serializer = ChatAdminSerializer(question)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        question.delete()
    return JsonResponse(status=status.HTTP_204_NO_CONTENT)

