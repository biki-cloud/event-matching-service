from django.shortcuts import render

# Create your views here.

from .models import Event
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Event, VendorProfile
from .forms import EventForm
import logging

logger = logging.getLogger('myapp')

def event_list(request):
    if request.user.is_anonymous:
        events = Event.objects.filter(status='published')
    elif request.user.role == 'イベント主催者':
        events = Event.objects.all()
    else:
        events = Event.objects.filter(status='published')
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    can_edit = False
    can_delete = False
    can_see_status = False
    can_apply = False

    if request.user.is_authenticated:
        if request.user.role == 'イベント主催者' and request.user.email == event.organizer.user.email:
            can_edit = True
            can_delete = True
            can_see_status = True
        elif request.user.role == 'イベント出店者':
            can_apply = True
        if request.user.is_superuser:
            can_edit = True
            can_delete = True

    context = {
        'event': event,
        'can_edit': can_edit,
        'can_delete': can_delete,
        'can_see_status': can_see_status,
        'can_apply': can_apply
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
def event_participation_request(request, event_pk):
    event = get_object_or_404(Event, pk=event_pk)
    vendor_profile = get_object_or_404(VendorProfile, user=request.user)
    if vendor_profile in event.vendors.all():
        messages.error(request, 'You have already applied to this event.')
    else:
        event.vendors.add(vendor_profile)
        messages.success(request, 'You have successfully applied to the event.')
    return redirect('event_detail', event.pk)
