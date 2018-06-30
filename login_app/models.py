from django.db import models

# Create your models here.
class AuthUsers(models.Model):
    user_name=models.CharField(max_length=58)
    user_password=models.CharField(max_length=58)
    def __str__(self):
        return "Пытался авторизироватся пользователь: %s %s" % (self.user_name, self.user_password)

    class Meta:
        verbose_name = 'Авторизированый'
        verbose_name_plural = 'Авторизированые'

