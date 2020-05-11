from django.urls import path, include
from . import views

app_name='blogs'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs' ),
    path('<int:blog_id>/', views.specific_blog, name='specific_blog' ),
]