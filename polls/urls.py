from django.urls import path
from . import views

urlpatterns = [
    # 127.0.0.1:8000 --> local
    # mydjangosite.com --> online
    path('', views.index, name='index'),
]
