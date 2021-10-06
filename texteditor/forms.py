from django import forms
from ckeditor.widgets import CKEditorWidget
from django.db.models import fields
from .models import Editor


class EditorForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget(), label="TextEditor")

    class Meta:
        model = Editor
        fields = "__all__"
