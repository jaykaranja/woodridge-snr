from django.db import models

# Create your models here.


class TourRequests(models.Model):
    full_names = models.CharField(max_length=50)
    phone_number = models.IntegerField(null=True)
    student_name = models.CharField(max_length=50)

    def __str__(self):
        return self.full_names
    
    class Meta:
        verbose_name_plural = "Tour requests"


class Applications(models.Model):
    student_first_name = models.CharField(max_length=10)
    student_second_name = models.CharField(max_length=10)
    student_class = models.CharField(max_length=5)
    kin_first_name = models.CharField(max_length=10)
    kin_surname = models.CharField(max_length=10)
    phone_number = models.IntegerField(null=True)
    any_med_condition =models.BooleanField(default=False)
    residence = models.CharField(max_length=20)

    def __str__(self):
        return f"{ self.student_first_name }  { self.student_second_name }"

    class Meta:
        verbose_name_plural = "Applications"

class Enquiries(models.Model):
    names = models.CharField(max_length=20)
    phone_number = models.IntegerField(null=True)
    query = models.CharField(max_length=50)

    def __str__(self):
        return self.names

    class Meta:
        verbose_name_plural = "Enquiries"