from django import forms
from .models import Employee, User
from django.core.exceptions import ValidationError
import re
from django.contrib.auth import authenticate


class EmployeeForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Employee
        fields = ["roll", "email", "username", "password", "address", "contact"]

    def clean_contact(self):
        contact = self.cleaned_data.get("contact")
        if not re.fullmatch(r"\d{10}", contact):
            raise ValidationError("contact number must be exactly 10 digits.")
        return contact

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email.endswith(".com"):
            raise ValidationError("Email must end with .com.")
        return email

    def clean_name(self):
        username = self.cleaned_data.get("username")
        if username:
            if len(username) < 4:
                raise ValidationError("userName must contain at least 4 characters.")
            if not username[0].isupper():
                raise ValidationError("userName must start with a capital letter.")
        return username


class LoginForm(forms.Form):
    print("inside loginform class")
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
