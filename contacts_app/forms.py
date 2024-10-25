from django import forms
from .models import Contact
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator


class ContactForm(forms.ModelForm):
    """
    Form for creating and editing contacts.

    Uses the Contact model and includes phone number and email verification.
    """
    class Meta:
        model = Contact
        fields = ['name', 'address', 'phone_number', 'email', 'birthday']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
        labels = {
            'name': 'Name',
            'address': 'Address',
            'phone_number': 'Phone number',
            'email': 'Email',
            'birthday': 'Birthday',
        }

    def clean_phone_number(self):
        """
        Phone number validation. Checks that the phone number is correct.

        Returns:
        str: Valid phone number.

        Raises:
        forms.ValidationError: If the phone number is incorrect.
        """
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number:
            raise ValidationError("This field is required.")

        return phone_number

    def clean_email(self):
        """
        Email validation. Checks that the email is correct
        and unique in the database.
        """
        email = self.cleaned_data.get('email')

        try:
            EmailValidator()(email)
        except ValidationError:
            raise ValidationError("Enter a valid email address.")

        # contact_id = self.instance.id
        # if Contact.objects.filter(email=email).exclude(id=contact_id).exists():
        #     raise ValidationError("This email address is already in use.")

        return email

class BirthdayFilterForm(forms.Form):
    """
    Форма для вибору періоду для фільтрації контактів з наближаючими днями народження.
    """
    PERIOD_CHOICES = [
        (1, '1 month'),
        (3, '3 months'),
        (6, '6 months'),
        (12, '1 year'),
    ]

    period = forms.ChoiceField(
        choices=PERIOD_CHOICES, initial=1, label="Choice period", widget=forms.Select(attrs={'class': 'form-control'})
    )
