from django.db import models


class Registry(models.Model):
    ticket_number = models.CharField(max_length=10)
    owner_name = models.TextField()
    owner_doc = models.TextField()
    date_issue = models.CharField(max_length=15)
