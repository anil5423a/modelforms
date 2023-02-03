from django import forms
from app.models import *
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class webpageForm(forms.ModelForm):
    class Meta:
        model=webpage
        fields='__all__'

class Accessrecords(forms.ModelForm):
    class Meta:
        model=Accessrecords
        fields='__all__'
