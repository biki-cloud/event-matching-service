from . import views
from django.urls import path

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('organizer_signup/', views.organizer_signup_view, name='organizer_signup'),
    path('organizer_login/', views.login_view, name='organizer_login'),
    path('organizer_profile/', views.organizer_profile_view, name='organizer_profile'),
]