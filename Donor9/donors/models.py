from django.db import models


class Donor(models.Model):
    """Holds the Donor information"""
    user = models.OneToOneField("auth.User")
    cnic = models.CharField(max_length=16, primary_key=True)
    phone = models.CharField(max_length=16)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    location = models.ForeignKey("Location")
    BLOOD_GROUP_CHOICES = (("A+", "A+"),
                          ("A-", "A-"),
                          ("B+", "B+"),
                          ("B-", "B-"),
                          ("AB+", "AB+"),
                          ("AB-", "AB-"),
                          ("O+", "O+"),
                          ("O-", "O"))
    blood_group = models.CharField(max_length=32, choices=BLOOD_GROUP_CHOICES)


class Location(models.Model):
    name = models.CharField(max_length=64)
