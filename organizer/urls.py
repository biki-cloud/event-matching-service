from django.urls import path

from . import views

urlpatterns = [
    path('create', views.OrganizerCreateView.as_view(), name="organizer_create"),
    path('detail/<int:pk>', views.OrganizerDetailView.as_view(), name="organizer_detail"),
]