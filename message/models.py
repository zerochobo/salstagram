from django.db import models
from membership.models import Member
from django.utils import timezone

# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(Member, related_name="message_sender", on_delete=models.CASCADE)
    recipient = models.ForeignKey(Member, related_name="message_receiver", on_delete=models.CASCADE)
    sentAt = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=150)
    isRead = models.BooleanField(default=False)

    objects = models.Manager()

    def save(self, **kwargs):
        if not self.id:
            self.sentAt = timezone.now() 
        super(Message, self).save(**kwargs)

    class Meta:
        ordering = ['-sentAt']

    def __str__(self):
        return self.content

    def summary(self):
        return self.content[:20]
