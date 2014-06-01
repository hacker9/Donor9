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
    '''General Area where a particular donor resides'''
    name = models.CharField(max_length=64)


class Donation(models.Model):
    '''Actual blood transaction'''
    donor = models.ForeignKey("Donor")
    date = models.DateField()
    remarks = models.TextField()


class SMS(models.Model):
    '''SMS communications with'''
    donor = models.ForeignKey("Donor")
    text = models.ForeignKey("SMSTemplate")
    RESPONSE_CHOICES = (("Yes", "Yes"), ("No", "No"), ("Maybe", "Maybe"))
    response = models.CharField(max_length=32, choices=RESPONSE_CHOICES)


class SMSTemplate(models.Model):
    '''Pre-made SMS templates'''
    text = models.CharField(max_length=140)
