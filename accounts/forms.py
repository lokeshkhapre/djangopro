from djnago import forms
from djnago.contrib.auth.forms import UserCreationForm
from djnago.contrib.auth.models import UserCreationForm

class SignUpForm(UserCreationForm):
  email = forms.CharField(max_length=254, required=True, widget=forms.Emailnput())

  class Meta: model = User fields = ('email','password1','password2')

 
