from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_id = models.EmailField()
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    confirm_password = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class StudentLogin(models.Model):
    email_id = models.EmailField()
    password = models.CharField(max_length=20)  
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student}'s login"