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
    user_otp=models.CharField(max_length=6)
    created = models.DateTimeField(auto_now_add=True)
    
class CaptchaData(models.Model):
    captcha_data = models.CharField(max_length=6)

    def __str__(self):
        return self.captcha_data