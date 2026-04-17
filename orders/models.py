# from django.db import models

# # Create your models here.


# def __str__(self):
#     return f"{self.name} - {self.date} {self.time}"


# class Order(models.Model):
#     name = models.CharField(max_length=100)
#     phone = models.CharField(max_length=20)
#     date = models.DateField()
#     time = models.TimeField()
#     guests = models.CharField(max_length=10)
#     zone = models.CharField(max_length=20)

#     created_at = models.DateTimeField(auto_now_add=True)


from django.db import models

class Order(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    guests = models.CharField(max_length=10)
    zone = models.CharField(max_length=50)