from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    email = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    full_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    subject = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))

    class Meta:
        model = Contact
        fields = [
            "email",
            "full_name",
            "subject",
            "message",
        ]  # Exclude auto-generated fields
