from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'w-full rounded-md p-2 mb-2 border border-blue-500'})

    class Meta:
        model = Book
        fields = '__all__'