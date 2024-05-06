from . import views
from django.urls import path

urlpatterns = [
    path('', views.accounts_home, name='accounts_home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
]