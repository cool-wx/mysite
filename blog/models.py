from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class BlogArticles(models.Model):
    title = models.CharField(max_length=300, verbose_name='标题')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name='作者')
    body = models.TextField(verbose_name='内容')
    publish = models.DateField(default=timezone.now, verbose_name='发布时间')

    class Meta:
        ordering = ('-publish',)

        def __str__(self):
            content = ""
            if len(self.body) > 100:
                content = self.body[0:100]
            else:
                content = self.body
            return self.title + " " + content

        def __repr__(self):
            return self.titile
