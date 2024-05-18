from django import forms

from .models import OrganizerProfile


class OrganizerCreateForm(forms.ModelForm):
    class Meta:
        # どのモデルをフォームにするか指定
        model = OrganizerProfile
        # そのフォームの中から表示するフィールドを指定
        fields = ("phone", "gender")

    # フォームを綺麗にするための記載
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
