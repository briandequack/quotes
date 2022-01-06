from django import forms
from quotes.models import Quote, Author
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):

    class Meta():
        model = User
        fields = ('email','password')

        widgets = {
            'email':forms.TextInput(attrs={'type':'email','class':'form-control','id':'floatingInput','placeholder':"name@example.com"}),
            'password':forms.PasswordInput(attrs={'type':'password','class':'form-control','id':'floatingPassword','placeholder':"Password"}),
        }




class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ('author','text')
        widget = {
            'author':forms.TextInput(attrs={'class':'form-label'}),
            'text':forms.Textarea(attrs={'class':'form-label'}),
        }


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name',)
