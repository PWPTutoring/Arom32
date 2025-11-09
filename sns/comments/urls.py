from django.urls import path
from . import views

app_name = 'comments' #앱 이름

urlpatterns = [
    path('', views.comment_view, name='comment'),
    path('signup/', views.signup_view, name='signup'),
]