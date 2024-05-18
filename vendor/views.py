from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib import messages

from .models import VendorProfile
from .forms import VendorCreateForm

class VendorDetailView(DetailView):
    model = VendorProfile
    template_name = 'vendor/vendor_detail.html'
    context_object_name = 'vendor'

class OrganizerCreateView(CreateView):
    model = VendorProfile
    template_name = 'vendor/vendor_create.html'
    form_class = VendorCreateForm
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
        form.instance.user = self.request.user  # ログインしているユーザーを OrganizerProfile の user に設定
        messages.success(self.request, 'イベント出店者情報を登録しました')
        return super().form_valid(form)
