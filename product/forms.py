from django import forms
from .models import Product,Category 

class ProductForm(forms.ModelForm):
    userid = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control d-none'}), label='')
    category = forms.ModelMultipleChoiceField(
            queryset=Category.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            )        
    class Meta:
        model = Product
        fields = ('title','subtitle','desc','marked_price','selling_price','product_image','product_image2','product_image3','offer_present','isActive','quantity','inStock','userid','category') 

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'subtitle': forms.TextInput(attrs={'class':'form-control'}),
            'desc': forms.Textarea(attrs={'class':'form-control','style':'height:200px','overflow':'auto'}),
        }
