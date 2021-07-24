from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.db import models
from django.forms import fields, widgets
from .models import User,Rolereq,Rooms,Bookings

class RegForm(UserCreationForm):

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control my-2","placeholder": "Enter Password"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control my-2","placeholder": "Confirm Password"
    }))
    class Meta:
        model = User
        fields = ["first_name","last_name","email","username","mobilenumber","uimg"]
        widgets = {
            "username":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Username",

            }),
            "first_name":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter First Name",
            }),
            "last_name":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Last name",
            }),
            "email":forms.EmailInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Email",
            }),
            "mobilenumber":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Mobile Number",
            }),
            "uimg":forms.FileInput(attrs={
                "class":"form-control my-2",
            }),

        }

class Chgepwd(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control my-2","placeholder": "Enter Old Password"
    }))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control my-2","placeholder": "Enter New Password"
    }))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control my-2","placeholder": "Confirm New Password"
    }))
    class Meta:
        model = User
        fields =  ["old_password","new_password1","new_password2"]

class Pfupd(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","mobilenumber","uimg"]
        widgets = {
            "username":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Username",
                "readonly":True
            }),
            "first_name":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter First Name",
            }),
            "last_name":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Last name",
            }),
            "email":forms.EmailInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Email",
            }),
            "mobilenumber":forms.TextInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Mobile Number",
            }),
            "uimg":forms.FileInput(attrs={
                "class":"form-control my-2",
            }),

        }

class Rltype(forms.ModelForm):
    class Meta:
        model = Rolereq
        fields= ["uname","rltype","pfe"]
        widgets= {
            # "uname":forms.TextInput(attrs={
            #     "class":"form-control my-2",
            #     "readonly":True,
            # }),
            "rltype":forms.Select(attrs={
                "class":"form-control my-2",

            })
        }

class Rlupd(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","role"]
        widgets= {
            "username":forms.TextInput(attrs={
                "class":"form-control my-2",
                "readonly":True
            }),
            "role":forms.Select(attrs={
                "class":"form-control my-2"
            })
        }

class RoomForm(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = ['rno','rdes','rcost','rimg']
        widgets = {
            "rno":forms.NumberInput(attrs={
                "class": "form-control my-2",
                "placeholder":"Enter The Room Number"
            }),
            "rdes":forms.Textarea(attrs= {
                "class":"form-control my-2",
                "placeholder":"Enter the Description of the room",
                "rows":"3"
            }),
            "rcost":forms.NumberInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter Price"
            }),
            "rimg":forms.FileInput(attrs={
                "class":"form-control my-2"
            })
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = ["sdate","edate"]
        widgets = {
            "sdate":forms.DateInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter The Start Date",
                "type":"date"
            }),
            "edate":forms.DateInput(attrs={
                "class":"form-control my-2",
                "placeholder":"Enter The End Date",
                "type":"date"
            }),
        }
