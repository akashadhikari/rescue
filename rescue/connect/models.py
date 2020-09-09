from django.db import models


class HelpCenter(models.Model):
    name = models.CharField(max_length=140)
    address = models.CharField(max_length=140)
    contact = models.CharField(max_length=15)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name