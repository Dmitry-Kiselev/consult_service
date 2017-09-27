from django.db import models
from django.conf import settings

from users.models import Department


class Conversation(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='conversations_as_sender')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE,
                                 related_name='conversations_as_receiver')


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages',
                                     on_delete=models.CASCADE)
    text = models.CharField(max_length=300)


class Queue(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,
                                   related_name='queue')
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
