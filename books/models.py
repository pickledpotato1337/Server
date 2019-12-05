from django.db import models


# Create your models here.

class PublicChatRoom(models.Model):
    chatId = models.IntegerField()
    chatName = models.CharField(max_length=45)


class PrivateChatRoom(models.Model):
    chatId = models.IntegerField()
    chatName = models.CharField(max_length=45)
    user1Id = models.IntegerField()
    user2Id = models.IntegerField()


class User(models.Model):
    userId = models.IntegerField()
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)


class ChatBan(models.Model):
    chatId = models.IntegerField()
    bannedUser = models.IntegerField()


class UserBlock(models.Model):
    blockingId = models.IntegerField()
    blockedId = models.IntegerField()


class ChatRoomUser(models.Model):
    chatId = models.IntegerField()
    userId = models.IntegerField()


class ChatAdmin(models.Model):
    chatId = models.IntegerField()
    adminId = models.IntegerField()
