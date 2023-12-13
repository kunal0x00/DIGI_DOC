from django import forms
from .models import User

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['file']
