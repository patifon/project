from django.db import models


# Create your models here.
class UserRegisterGroup(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    password_repeat=models.CharField(max_length=50)

    def __str__(self):
        return "Пользователь: %s %s" % (self.name, self.email)

    class Meta:
        verbose_name = 'MyUser'
        verbose_name_plural = 'A lot of Users'



