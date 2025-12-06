from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import BlogPost, Comment, Profile


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email (optional)"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm password"}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ("title", "content")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(
                attrs={"rows": 6, "class": "form-control", "placeholder": "Write your story..."}
            ),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)
        widgets = {
            "content": forms.Textarea(
                attrs={"rows": 3, "class": "form-control", "placeholder": "Add a thoughtful comment"}
            ),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bio", "location", "website")
        widgets = {
            "bio": forms.Textarea(attrs={"rows": 4, "class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "website": forms.URLInput(attrs={"class": "form-control"}),
        }


