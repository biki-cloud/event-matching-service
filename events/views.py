from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy

from .models import Event
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class EventList(ListView):
    model = Event
    context_object_name = 'events'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class EventDetail(DetailView):
    model = Event
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class EventCreate(CreateView):
    model = Event
    fields = ['name', 'date', 'location', 'description']
    success_url = '/events/list'

    def form_valid(self, form):
        # ログインしているユーザーをオーガナイザーとして設定
        form.instance.organizer = self.request.user.organizer_profile
        return super().form_valid(form)


class EventUpdate(UpdateView):
    model = Event
    fields = ['name', 'date', 'location', 'description']
    success_url = '/events/list'
    template_name_suffix = "_update_form"


class EventDelete(DeleteView):
    model = Event
    success_url = '/events/list'
