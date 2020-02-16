from django import forms
from .models import Attendee

class AttendeeForm(forms.ModelForm):

	class Meta:
		model = Attendee
		exclude = ('login_Date', )