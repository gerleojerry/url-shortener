from django import forms
from .models import Links

class LinkForm(forms.ModelForm):

  class Meta: 
    model = Links
    fields = ['link']