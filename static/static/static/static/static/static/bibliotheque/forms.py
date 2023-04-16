from django import forms
from bibliotheque.models import Book


class ContactForm(forms.Form):
    name = forms.CharField(
        min_length=3, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    email = forms.EmailField(
        max_length=100, widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    subject = forms.CharField(
        min_length=5,
        max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 3})
    )


class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields = [ 
                "title", 
                "autor",
                "category", 
                "image",
                "exemplaire",
                "body",
                "manager",]
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

        for (element,field) in self.fields.items():
            field.widget.attrs.update({"class" : 'form-control'})
                

        