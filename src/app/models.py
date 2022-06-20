from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from phone_field import PhoneField
from django.core.validators import RegexValidator, MinLengthValidator

class User(AbstractUser):
    is_district = models.BooleanField(default=False)
    is_subdiv = models.BooleanField(default=False)
    is_circle = models.BooleanField(default=False)
    is_citizen = models.BooleanField(default=False)


class District(models.Model):
    dist_id = models.CharField(primary_key=True, max_length=2)
    dist_name = models.CharField(max_length=40)
    dist_name_hn = models.CharField(max_length=40)

    class Meta:
        db_table = 'district'
        ordering = ["dist_id"]

    def __str__(self):
        return f"{self.dist_name_hn}"

class SubDiv(models.Model):
    subdiv_id = models.CharField(max_length=2, primary_key=True)
    subdiv_name = models.CharField(max_length=20)
    subdiv_name_hn = models.CharField(max_length=20)
    district = models.ForeignKey(District, models.DO_NOTHING, null=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete= models.DO_NOTHING,
        null=True
    )

    class Meta:
        db_table = 'subdiv'
        ordering = ['subdiv_id']

    def __str__(self):
        return f"{self.subdiv_name_hn}"

class Circle(models.Model):
    circle_id = models.CharField(primary_key=True, max_length=3)
    circle_name = models.CharField(max_length=40)
    circle_name_hn = models.CharField(max_length=40)
    subdiv = models.ForeignKey(SubDiv, models.DO_NOTHING, null=True)
    district = models.ForeignKey(District, models.DO_NOTHING, null=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete= models.DO_NOTHING,
        null=True
    )
    short_name = models.CharField(max_length=3, null=True, blank=True)

    class Meta:
        db_table = 'circle'
        ordering = ["circle_id"]

    def __str__(self):
        return f"{self.circle_name_hn}"

class Panchayat (models.Model):
    panchayat_name = models.CharField(max_length=40)
    panchayat_name_hn = models.CharField(max_length=40)
    district = models.ForeignKey(District, models.DO_NOTHING, to_field='dist_id')
    circle = models.ForeignKey(Circle, models.DO_NOTHING, to_field='circle_id')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.DO_NOTHING,
        null=True
    )

    class Meta:
        db_table = 'panchayat'
        ordering = ["panchayat_name"]

    def __str__(self):
        return f"{self.panchayat_name_hn}"