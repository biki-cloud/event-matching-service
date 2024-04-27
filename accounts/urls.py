from . import views
from django.urls import path

urlpatterns = [
    path('', views.accounts_home, name='accounts_home'),
    path('organizer_login/', views.organizer_login, name='organizer_login'),
    path('organizer_profile/', views.organizer_profile, name='organizer_profile'),
    path('organizer_signup/', views.organizer_signup, name='organizer_signup'),
]