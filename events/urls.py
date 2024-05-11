
from django.urls import path

from .views import (
    event_list,
    event_detail,
    create_event,
    update_event,
    delete_event,
    event_participation_request
)

urlpatterns = [
    path("", event_list, name="events_home"),
    path("list", event_list, name="event_list"),
    path('create', create_event, name="event_create"),
    path("<int:pk>/detail", event_detail, name="event_detail"),
    path('<int:pk>/update/', update_event, name='event_update'),
    path('<int:pk>/delete/', delete_event, name='event_delete'),
    path('event_participation_request/<int:event_pk>/', event_participation_request, name='event_participation_request')
]