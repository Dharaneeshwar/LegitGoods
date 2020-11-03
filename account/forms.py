from django import forms
from .models import User 

class UserForm(forms.ModelForm):
    userid = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control d-none'}), label='')
    class Meta:
        model = User
        fields = '__all__' 
        widgets = {
            'phone_number': forms.NumberInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),            
            'address': forms.Textarea(attrs={'class':'form-control','style':'height:200px','overflow':'auto'}),            
            'country': forms.TextInput(attrs={'class':'form-control'}),            
            'state': forms.TextInput(attrs={'class':'form-control'}),            
            'pincode': forms.NumberInput(attrs={'class':'form-control'}),            
        }
