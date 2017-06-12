from django import forms
from polls.models import Candidate

class ContactDetails(forms.Form):
	contact_name = forms.CharField(required= True)
	
	class Meta:
		model = Candidate
		fields = ('contact_name',)
