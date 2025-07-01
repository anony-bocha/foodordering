from django import forms

class CheckoutForm(forms.Form):
    customer_name = forms.CharField(max_length=100, label="Name")
    customer_email = forms.EmailField(label="Email")
    customer_address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), label="Address")
