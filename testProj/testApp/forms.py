from django import forms

from .models import Timeline

class TimelineForm(forms.ModelForm):
    class Meta:
        model = Timeline
        fields = [
            'headline',
            'text',
            'event_date'
        ]