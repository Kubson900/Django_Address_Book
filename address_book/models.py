from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Contact(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    date_of_modification = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' ' + self.surname

    def get_absolute_url(self):
        return reverse('contact-detail', kwargs={'pk': self.pk})

