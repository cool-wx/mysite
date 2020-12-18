from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, verbose_name='用户')
    birth = models.DateField(blank=True, null=True, verbose_name='出生日期')
    phone = models.CharField(max_length=20, null=True, verbose_name='电话号码')

    class Meta:
        verbose_name = verbose_name_plural = "用户扩展信息"

    def __str__(self):
        return 'User %s' % self.user.username
