from django import forms
from .models import Borrow

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = ['book']



class ReturnBookForm(forms.Form):
    confirm = forms.BooleanField(label="Confirm you want to return this book")
