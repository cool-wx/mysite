from django.urls import path
from blog import views

urlpatterns = [
    path('index/', views.index, name='blog_index'),
    path('title/', views.blog_title, name='blog_title'),
    path('blog/<int:article_id>', views.blog_article, name='blog_article')
]
