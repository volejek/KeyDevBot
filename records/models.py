from django.db import models

# Create your models here.
class ArrivalRecord(models.Model):
    date = models.DateTimeField()
    username = models.CharField(max_length=255)
    text = models.TextField()
    comment_date = models.DateTimeField()
    message_id = models.CharField(max_length=255, unique=True)
    parent_message_id = models.CharField(max_length=255, null=True, blank=True)
    chat_id = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.username}: {self.text} - {self.comment_date.strftime('%Y-%m-%d %H:%M:%S')}"
    