from django.urls import path
from .import views

app_name = 'accounts_app'
urlpatterns = [
    path('register', views.user_register, name = 'user_registers'),
    path('bcv/', views.ListUserBaseView.as_view(), name = 'list_user'),
    path('login/', views.login_user, name = 'login'),
    path('logout/', views.user_logout, name = 'logout'), 
]