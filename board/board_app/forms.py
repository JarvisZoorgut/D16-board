from django import forms
from django.core.exceptions import ValidationError

from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(min_length=30)

    class Meta:
        model = Article
        fields = ['title', 'text', 'category', 'upload']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        content = cleaned_data.get("text")

        if title == content:
            raise ValidationError(
                "Заголовок не должен быть идентичен содержанию."
            )

        return cleaned_data
