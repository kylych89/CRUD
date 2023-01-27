from django.urls import path

from .views import register_user, login_user, logout_user

app_name = 'account'

urlpatterns = [
    path('', register_user, name='register_user'),
    path('login_user/', login_user, name='login_user'),
    path('logout_user/', logout_user, name='logout_user'),

]
