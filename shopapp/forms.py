from django import forms
from django.forms import TextInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import profile, order, contact

# -------- Registration ----------
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        ]

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

# -------- Login ----------
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)

# -------- EditProfile_pic ----------
class EditprofileForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]

# -------- EditProfile_pic ----------
class EditProfilePicForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = [
            'image',
        ]

# -------- Order product ----------
class OrderProductForm(forms.ModelForm):
    class Meta:
        model = order
        fields = [
            'phone_number',
            'product_code',
            'quantity',
            'order_place',
            'order_date',
            'delivery_date',
        ]

class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = [
            'email',
            'message'
        ]
        widgets = {'email': TextInput(attrs={'placeholder': 'Enter your email'})}

