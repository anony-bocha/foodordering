from django import forms


class CheckoutForm(forms.Form):
    customer_name = forms.CharField(
        max_length=100,
        label="Full Name",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your full name",
                "required": True,
            }
        ),
    )
    customer_email = forms.EmailField(
        label="Email Address",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your email",
                "required": True,
            }
        ),
    )
    customer_address = forms.CharField(
        label="Delivery Address",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your delivery address",
                "rows": 3,
                "required": True,
            }
        ),
    )
