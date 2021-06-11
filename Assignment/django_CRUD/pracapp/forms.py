from django import forms
from .models import *


class Book_form(forms.ModelForm):

    class Meta:
        model = Detials
        fields = ('authorname','book_price','genre','title')
        labels = {
            'authorname':'Author Name',
            'genre':'Genre'
        }
    def __init__(self, *args, **kwargs):
        super(Book_form,self).__init__(*args, **kwargs)
        self.fields['title'].empty_label = "Select"
        self.fields['book_price'].required = False

    