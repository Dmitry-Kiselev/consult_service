from django.db.models import Q
from rest_framework import viewsets

from chat.models import Conversation, Message, Queue
from .serializers import ConversationSerializer, MessageSerializer, \
    QueueSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    def get_queryset(self):
        return Q(Message.objects.filter(
            receiver=self.request.user)) | Q(
            Message.objects.filter(sender=self.request.user))


class MessageSerializerViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Q(Message.objects.filter(
            conversation__receiver=self.request.user)) | Q(
            Message.objects.filter(conversation__sender=self.request.user))


class QueueSerializerViewSet(viewsets.ModelViewSet):
    queryset = Queue.objects.all()
    serializer_class = QueueSerializer

    def get_queryset(self):
        return Queue.objects.filter(department=self.request.user.department)
