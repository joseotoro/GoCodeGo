from django import forms

class UserForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=30, required=False)
    last_name = forms.CharField(label='Last name', max_length=30, required=False)
    username = forms.CharField(label='Username', max_length=30)
    bio = forms.CharField(label='Bio', max_length=150, required=False)
    website = forms.CharField(label='Website', max_length=80, required=False)
    twitter = forms.CharField(label='Twitter', max_length=80, required=False)
    facebook = forms.CharField(label='Facebook', max_length=80, required=False)
    linkedin = forms.CharField(label='LinkedIn', max_length=80, required=False)
    github = forms.CharField(label='Github', max_length=80, required=False)
