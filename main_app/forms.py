from django import forms
from .models import Feeding

class FeedingForm(forms.ModelForm):
    #The meta class allows us to provide custom behaviour and settings to the generic model 
    #form class wihtout altering or overrriding its
    #this is an example of meta programming
    class Meta:
        model = Feeding
        fields = ['date', 'meal'] 
        widgets = {
            'date': forms.DateInput(
                format=('%y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }