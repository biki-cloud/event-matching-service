from django.urls import path

from .views import EventList, EventDetail, EventCreate, EventUpdate, EventDelete

urlpatterns = [
    path("", EventList.as_view(), name="events_home"),
    path("list", EventList.as_view(), name="event_list"),
    path('create', EventCreate.as_view(), name="event_create"),
    path("<int:pk>/detail", EventDetail.as_view(), name="event_detail"),
    path('<int:pk>/update/', EventUpdate.as_view(), name='event_update'),
    path('<int:pk>/delete/', EventDelete.as_view(), name='event_delete'),
]