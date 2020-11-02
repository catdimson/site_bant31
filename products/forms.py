from django import forms
from .models import Subscribers

class SubscrubersForm(forms.ModelForm):
    class Meta():
        model = Subscribers  #название модели
        #fields = [''] включение полей или исключать eclude, по ситуации
        exclude = ['']
