from django import forms
from .models import Post
from django.utils.text import slugify

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']

    # ولیدیشن روی یک فیلد
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise forms.ValidationError('عنوان باید حداقل ۵ کاراکتر باشد.')
        return title

    # ولیدیشن چند فیلدی
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        body = cleaned_data.get('body')

        if title and body and title.lower() in body.lower():
            raise forms.ValidationError('عنوان نباید داخل متن تکرار شود.')
        return cleaned_data
