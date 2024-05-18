from django.contrib import messages
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from .forms import OrganizerCreateForm
from .models import OrganizerProfile


class OrganizerDetailView(DetailView):
    model = OrganizerProfile
    template_name = "organizer/organizer_detail.html"
    context_object_name = "organizer"


class OrganizerUpdateView(UpdateView):
    model = OrganizerProfile
    form_class = OrganizerCreateForm
    template_name = "organizer/organizer_update.html"

    def get_success_url(self):
        return reverse("organizer_detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        messages.success(self.request, "主催者情報が更新されました。")
        return super().form_valid(form)
