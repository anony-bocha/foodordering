from django import forms

class CheckoutForm(forms.Form):
    customer_name = forms.CharField(max_length=100)
    customer_email = forms.EmailField()
    customer_address = forms.CharField(widget=forms.Textarea)
