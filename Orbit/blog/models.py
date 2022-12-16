from django.db import models

# Create your models here.


class Home(models.Model):
    image = models.ImageField()
    content = models.CharField(max_length=202)

    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.content


class About(models.Model):
    title = models.CharField(max_length=202)
    image = models.ImageField()
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


class Degree(models.Model):
    name = models.CharField(max_length=202)
    percentage = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=202)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField()
    title = models.CharField(max_length=202)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Service(models.Model):
    icon = models.CharField(max_length=202)
    name = models.CharField(max_length=100)
    title = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Work(models.Model):
    title = models.CharField(max_length=202)
    location = models.CharField(max_length=202)
    address = models.CharField(max_length=202)
    data = models.CharField(max_length=202)


    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Education(models.Model):
    title = models.CharField(max_length=203)
    location = models.CharField(max_length=202)
    address = models.CharField(max_length=202)
    data = models.CharField(max_length=202)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Happy_Client(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=202)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Medium(models.Model):
    data = models.CharField(max_length=100)
    title = models.CharField(max_length=202)
    link = models.CharField(max_length=404)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


