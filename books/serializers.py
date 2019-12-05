from rest_framework import serializers
from .models import PublicChatRoom, PrivateChatRoom, User, ChatBan, UserBlock, ChatRoomUser, ChatAdmin

class PublicChatRoomSerializer(serializers.Serializer):
    chatId = serializers.IntegerField()
    chatName = serializers.CharField(max_length=45)


class PrivateChatRoomSerializer(serializers.Serializer):
    chatId = serializers.IntegerField()
    chatName = serializers.CharField(max_length=45)
    user1Id = serializers.IntegerField()
    user2Id = serializers.IntegerField()

class UserSerializer(serializers.Serializer):
    userId = serializers.IntegerField()
    username = serializers.CharField(max_length=45)
    password = serializers.CharField(max_length=45)

class ChatBanSerializer(serializers.Serializer):
    chatId = serializers.IntegerField()
    userId = serializers.IntegerField()

class UserBlockSerializer(serializers.Serializer):
    blockingId = serializers.IntegerField()
    blockedId = serializers.IntegerField()

class ChatRoomUserSerializer(serializers.Serializer):
    chatId = serializers.IntegerField()
    userId = serializers.IntegerField()

class ChatAdminSerializer(serializers.Serializer):
    chatId = serializers.IntegerField()
    adminId = serializers.IntegerField()
