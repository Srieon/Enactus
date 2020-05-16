from django.urls import path
from . import views


app_name = "form_valid"

urlpatterns = [
    path('register/',views.register,name= 'register'),
    path('user_login/',views.user_login,name='user_login')
]
