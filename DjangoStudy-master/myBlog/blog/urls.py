#from ssl import VERIFY_ALLOW_PROXY_CERTS
from django.urls import path
from . import views   # 현재 폴더의 views.py를 사용할 수 있게 가져온다.

urlpatterns = [
    path('', views.index),
]