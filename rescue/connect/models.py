from django.db import models


class Need(models.Model):
    requirement = models.CharField(max_length=100)

    def __str__(self):
        return self.requirement


class Info(models.Model):
    name = models.CharField(max_length=140)
    address = models.CharField(max_length=140)
    contact = models.CharField(max_length=15)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class HelpCenter(Info):

    needs = models.ManyToManyField(Need, related_name="help_center_provisions")

    def __str__(self):
        return self.name


class Help(Info):

    needs = models.ManyToManyField(Need, related_name="help_provisions")

    def __str__(self):
        return self.name


class SomeoneNeedsHelp(Info):

    needs = models.ManyToManyField(Need, related_name="need_help")
    number_of_people = models.CharField(max_length=10)

    def __str__(self):
        return self.name