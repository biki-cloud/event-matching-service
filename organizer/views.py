from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib import messages

from .models import OrganizerProfile
from .forms import OrganizerCreateForm

class OrganizerDetailView(DetailView):
    model = OrganizerProfile
    template_name = 'organizer/organizer_detail.html'
    context_object_name = 'organizer'

class OrganizerCreateView(CreateView):
    model = OrganizerProfile
    template_name = 'organizer/organizer_create.html'
    form_class = OrganizerCreateForm
    success_url = '/events/list'

    # ログインしているユーザーを context に追加
    # contextに値を入れることで、テンプレートに値を渡し、テンプレートで表示することができる
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

    # フォームのバリデーションが成功した場合に呼ばれるメソッド
    # ここでフォームの内容を保存する
    def form_valid(self, form):
        # if self.request.user.organizer_profile.exists() is False:
            # ログインしているユーザーが OrganizerProfile を持っていない場合
            # OrganizerProfile の user にログインしているユーザーを設定し保存
        form.instance.user = self.request.user  # ログインしているユーザーを OrganizerProfile の user に設定
        messages.success(self.request, '主催者情報を登録しました')
        return super().form_valid(form)
