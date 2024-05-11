from django.http import HttpResponseForbidden
from django.shortcuts import render

# Create your views here.

from .models import Event
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import (
    Event,
    VendorProfile,
    EventApplication
)
from .forms import EventForm, EventApplicationForm
import logging

logger = logging.getLogger('myapp')

def event_list(request):
    if request.user.is_anonymous:
        events = Event.objects.filter(status='published')
    elif request.user.role == 'organizer':
        events = Event.objects.all()
    else:
        events = Event.objects.filter(status='published')
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    organizer_can_edit = False
    organizer_can_delete = False
    organizer_can_see_status = False
    vendor_can_apply = False
    request_non_approved_applications = EventApplication.objects.filter(is_approved=False)
    request_approved_applications = EventApplication.objects.filter(is_approved=True)

    if request.user.is_authenticated:
        if request.user.role == 'organizer' and request.user.email == event.organizer.user.email:
            organizer_can_edit = True
            organizer_can_delete = True
            organizer_can_see_status = True
        elif request.user.role == 'イベント出店者' and not event.vendors.filter(user=request.user).exists():
            vendor_can_apply = True
        if request.user.is_superuser:
            organizer_can_edit = True
            organizer_can_delete = True

    context = {
        'event': event,
        'organizer_can_edit': organizer_can_edit,
        'organizer_can_delete': organizer_can_delete,
        'organizer_can_see_status': organizer_can_see_status,
        'vendor_can_apply': vendor_can_apply,
        'event_application_form': EventApplicationForm(),
        'request_non_approved_applications': request_non_approved_applications,
        'request_approved_applications': request_approved_applications,
    }
    return render(request, 'events/event_detail.html', context)

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user.organizer_profile  
            event.save()
            return redirect(to='/events/')
    else:
        form = EventForm()
    return render(request, 'events/event_create.html', {'form': form})


def update_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_update.html', {'form': form})


def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect(to='/events/')
    return render(request, 'events/event_confirm_delete.html', {'event': event})


# 出店者からイベント申請リクエスト
@login_required
def request_application(request, event_pk):
    event = get_object_or_404(Event, pk=event_pk)
    vendor_profile = get_object_or_404(VendorProfile, user=request.user)
    form = EventApplicationForm(request.POST or None)
    if form.is_valid():
        # ２重申請リクエストが起きないようにする
        if event.applications.filter(vendor=vendor_profile).exists():
            messages.error(request, 'You have already applied for this event.')
            return redirect('event_detail', event.pk)
        application = form.save(commit=False)
        application.event = event
        application.vendor = vendor_profile
        application.save()
        messages.success(request, 'Your application has been submitted for review.')
        return redirect('event_detail', event.pk)
    return render(request, 'events/event_apply_create.html', {'form': form, 'event': event})

# イベント申請リクエストを承認
@login_required
def approve_application(request, application_id):
    application = get_object_or_404(EventApplication, id=application_id)
    if request.user != application.event.organizer.user:
        return HttpResponseForbidden()
    application.is_approved = True
    application.event.vendors.add(application.vendor)
    application.save()
    messages.success(request, 'The application has been approved.')
    return redirect('event_detail', application.event.pk)
