from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy

from .models import Event
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Event
from .models import VendorProfile
import logging

logger = logging.getLogger('django')


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
    fields = ['name', 'date', 'location', 'description', 'image', 'status', 'is_finished']
    success_url = '/events/list'
    template_name = 'events/event_create.html'

    def form_valid(self, form):
        # ログインしているユーザーをオーガナイザーとして設定
        form.instance.organizer = self.request.user.organizer_profile
        return super().form_valid(form)


class EventUpdate(UpdateView):
    model = Event
    fields = ['name', 'date', 'location', 'description', 'image', 'status', 'is_finished']
    success_url = '/events/list'
    template_name = 'events/event_update.html'


class EventDelete(DeleteView):
    model = Event
    success_url = '/events/list'


# 出店者からイベント申請リクエスト
@login_required
def event_participation_request(request, event_pk):
    event = get_object_or_404(Event, pk=event_pk)
    vendor_profile = get_object_or_404(VendorProfile, user=request.user)
    if vendor_profile in event.vendors.all():
        messages.error(request, 'You have already applied to this event.')
    else:
        event.vendors.add(vendor_profile)
        messages.success(request, 'You have successfully applied to the event.')
    return redirect('event_detail', event.pk)
