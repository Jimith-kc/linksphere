from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

from django import forms

from social.models import UserProfile,Posts,Comments,Stories


class RegistrationForm(UserCreationForm):
    
    class Meta:
        model=User
        fields=["username","email","password1","password2"]


class LoginForm(forms.Form):  #only call Form becouse we only want login no change or update needed
    #so no need of meta model fields
    username=forms.CharField()  
    password=forms.CharField()


class UserProfileForm(forms.ModelForm):

    class Meta:
        model=UserProfile
        exclude=('user','following','block')
        widgets={
            "dob":forms.DateInput(attrs={"class":"form-control","type":"date"})
        }


class PostForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=["title","post_image"]


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=["text"]


class StoryForm(forms.ModelForm):
    class Meta:
        model=Stories
        fields=["title","post_image"]