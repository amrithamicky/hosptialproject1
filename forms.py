from django import forms

from hsptlapp.models import Booking


class bookform(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'




