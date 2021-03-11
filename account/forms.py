from .models import Profile, Order
from django.contrib.auth.models import User
from django import forms


"""
Forms for Django authentication and authorisation:
- LoginForm, uses Django DB Table auth_user.
- UserRegistrationForm, uses Django DB Table auth_user and User created table
 account_profile
- UserEditForm, uses Django DB Table auth_user.
- ProfileEditForm, uses DB Table account_profile.
(- CommentForm, uses DB Table account_comment)
"""


class LoginForm(forms.Form):
    """
    Django LoginForm to authenticate the user.
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    """
    UserRegistrationForm to register the user.
    Validates the password by entering it twice, ensuring they match.
    Provides the 'username', first_name, and email fields.
    """
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    """
    Edit/Update the Character Profile.
    """
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    """
    Edit/Update the Character Profile.
    """
    class Meta:
        model = Profile
        fields = ('address', 'post_code', 'city')


class OrderCommentForm(forms.ModelForm):
    """
    """
    class Meta:
        model = Order
        fields = ('id', 'rating', 'comment')
