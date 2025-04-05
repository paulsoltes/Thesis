from django import forms
from .models import Schedule

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['timetable', 'instructor', 'room', 'subject', 'course', 'section', 'start_time', 'end_time']
