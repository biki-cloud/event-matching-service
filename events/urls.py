from django.urls import path

from .views import (check_application, create_event, delete_event,
                    event_detail, event_list, request_application,
                    update_event)

urlpatterns = [
    path("", event_list, name="events_home"),
    path("list", event_list, name="event_list"),
    path("create", create_event, name="event_create"),
    path("<int:pk>/detail", event_detail, name="event_detail"),
    path("<int:pk>/update/", update_event, name="event_update"),
    path("<int:pk>/delete/", delete_event, name="event_delete"),
    path(
        "event/<int:event_pk>/apply/", request_application, name="request_application"
    ),
    path(
        "check_application/<int:application_id>/",
        check_application,
        name="check_application",
    ),
]
