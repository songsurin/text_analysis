from django.db import models

class Chat(models.Model):
    idx = models.AutoField(primary_key=True)
    query = models.CharField(max_length=500, null=False)
    answer = models.CharField(max_length=1000, null=False)
    intent = models.CharField(max_length=50, null=False)
    tf = models.CharField(max_length=50, null=False)