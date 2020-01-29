
from .models import User, PublicChatRoom, PrivateChatRoom, ChatBan, UserBlock, ChatRoomUser, ChatAdmin
from .serializers import UserSerializer, PublicChatRoomSerializer, PrivateChatRoomSerializer, ChatBanSerializer,  UserBlockSerializer, ChatRoomUserSerializer, ChatAdminSerializer


from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.template import loader

from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import logout


def index(request):
    latest_question_list = User.objects.order_by('-userId')[:5]
    template = loader.get_template('books/index.html')
    context = {'latest_question_list': latest_question_list,
               }
    return HttpResponse(template.render(context, request))

class User_list(APIView):

   permission_classes = [IsAuthenticated]

   def get(self, request, format=None):

       questions = User.objects.all()
       serializer = UserSerializer(questions, many=True)
       return Response(serializer.data)

   def post(self, request, format=None):
       serializer = UserSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save(owner=self.request.user)
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class User_detail(APIView):
   permission_classes = [IsAuthenticated]

   def get_object(self, pk):
       try:
           return User.objects.get(pk=pk)
       except User.DoesNotExist:
           raise Http404

   def get(self, request, pk, format=None):
       question = self.get_object(pk)
       serializer = UserSerializer(question)
       return Response(serializer.data)

   def put(self, request, pk, format=None):
       question = self.get_object(pk)
       serializer = UserSerializer(question, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   def delete(self, request, pk, format=None):
       question = self.get_object(pk)
       question.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)


class PublicChatRoom_list(APIView):
     permission_classes = [IsAuthenticated]

     def get(self, request, format=None):
         questions = PublicChatRoom.objects.all()
         serializer = PublicChatRoomSerializer(questions, many=True)
         return Response(serializer.data)

     def post(self, request, format=None):
         serializer = PublicChatRoomSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save(owner=self.request.user)
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PublicChatRoom_detail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return PublicChatRoom.objects.get(pk=pk)
        except PublicChatRoom.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = PublicChatRoomSerializer(question)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = PublicChatRoomSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PrivateChatRoom_list(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        questions = PrivateChatRoom.objects.all()
        serializer = PrivateChatRoomSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PrivateChatRoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PrivateChatRoom_detail(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return PrivateChatRoom.objects.get(pk=pk)
        except PrivateChatRoom.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = PrivateChatRoomSerializer(question)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = PrivateChatRoomSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ChatBan_list(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        questions = ChatBan.objects.all()
        serializer = ChatBanSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ChatBanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChatBan_detail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return ChatBan.objects.get(pk=pk)
        except ChatBan.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = ChatBanSerializer(question)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = ChatBanSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserBlock_list(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        questions = UserBlock.objects.all()
        serializer = UserBlockSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserBlockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserBlock_detail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return UserBlock.objects.get(pk=pk)
        except UserBlock.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = UserBlockSerializer(question)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = UserBlockSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ChatRoomUser_list(APIView):

    permission_classes = [IsAuthenticated]


    def get(self, request, format=None):
        questions = ChatRoomUser.objects.all()
        serializer = ChatRoomUserSerializer(questions, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = ChatRoomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChatRoomUser_detail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return ChatRoomUser.objects.get(pk=pk)
        except ChatRoomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = ChatRoomUserSerializer(question)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = ChatRoomUserSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ChatAdmin_list(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        questions = ChatAdmin.objects.all()
        serializer = ChatAdminSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ChatAdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChatAdmin_detail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return ChatAdmin.objects.get(pk=pk)
        except ChatAdmin.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = ChatAdminSerializer(question)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = ChatAdminSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


