from django import forms
from subscription.models import Subscription

class SubscritionForm(forms.ModelForm):
	class Meta:
		model = Subscription
		exclude = ('created_at',)
