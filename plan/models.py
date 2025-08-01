from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class TimeUntilDone(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Plan(models.Model):
    class Status(models.TextChoices):
        NotDone = "Not done"
        Done = "Done"
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    time_until_done = models.ForeignKey(TimeUntilDone, on_delete=models.CASCADE)
    body = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)
    status = models.CharField(choices=Status.choices, default=Status.NotDone)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('details', args=[self.slug])



