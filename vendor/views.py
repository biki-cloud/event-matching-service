from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib import messages
from django.urls import reverse_lazy, reverse

from .models import VendorProfile
from .forms import VendorCreateForm

class VendorDetailView(DetailView):
    model = VendorProfile
    template_name = 'vendor/vendor_detail.html'
    context_object_name = 'vendor'

class VendorUpdateView(UpdateView):
    model = VendorProfile
    form_class = VendorCreateForm
    template_name = 'vendor/vendor_update.html'

    def get_success_url(self):
        return reverse('vendor_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        messages.success(self.request, '出店者情報が更新されました。')
        return super().form_valid(form)
