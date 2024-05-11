from django.urls import path

from .views import (
    event_list,
    event_detail,
    create_event,
    update_event,
    delete_event,
    request_application,
    approve_application
)

urlpatterns = [
    path("", event_list, name="events_home"),
    path("list", event_list, name="event_list"),
    path('create', create_event, name="event_create"),
    path("<int:pk>/detail", event_detail, name="event_detail"),
    path('<int:pk>/update/', update_event, name='event_update'),
    path('<int:pk>/delete/', delete_event, name='event_delete'),
    path('event/<int:event_pk>/apply/', request_application, name='request_application'),
    path('approve_application/<int:application_id>/', approve_application, name='approve_application')
]