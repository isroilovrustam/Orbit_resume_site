from django.db import models

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=202)
    last_name = models.CharField(max_length=202)
    email = models.CharField(max_length=202)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class ContactMe(models.Model):
    address = models.CharField(max_length=202)
    phoneone = models.CharField(max_length=200)
    phonetwo = models.CharField(max_length=200)
    email = models.EmailField()
    website = models.CharField(max_length=202)

    def __str__(self):
        return self.website