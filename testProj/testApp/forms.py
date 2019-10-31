from django import forms

from .models import Timeline

class TimelineForm(forms.ModelForm):
    class Meta:
        model = Timeline
        fields = '__all__'
        widgets = {
            'event_date': forms.DateInput(attrs={'type': 'date'})
        }