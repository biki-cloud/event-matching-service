from django.urls import path

from . import views

urlpatterns = [
    path(
        "update/<int:pk>", views.OrganizerUpdateView.as_view(), name="organizer_update"
    ),
    path(
        "detail/<int:pk>", views.OrganizerDetailView.as_view(), name="organizer_detail"
    ),
]
