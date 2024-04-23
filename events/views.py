from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import Event
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class EventList(ListView):
    model = Event
    context_object_name = 'events'


class EventDetail(DetailView):
    model = Event
    context_object_name = 'event'


class EventCreate(CreateView):
    model = Event
    fields = ['name', 'date', 'location', 'description']
    success_url = '/events/list'


class EventUpdate(UpdateView):
    model = Event
    fields = ['name', 'date', 'location', 'description']
    success_url = '/events/list'
    template_name_suffix = "_update_form"


class EventDelete(DeleteView):
    model = Event
    success_url = '/events/list'
