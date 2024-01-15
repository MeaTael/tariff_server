from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    phoneNumber = models.CharField("Phone number", max_length=11)
    operator = models.TextField("Operator")
    minutesOption = models.IntegerField("Minutes option")
    internetOption = models.IntegerField("Internet option")
    rent = models.BooleanField("Rent")
    redeem = models.BooleanField("Redeem")
    socials = ArrayField(models.BooleanField("Social"), size=5)
    totalAmount = models.IntegerField("Total Amount")

    def __str__(self):
        return self.phoneNumber
