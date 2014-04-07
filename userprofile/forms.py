from models import UserProfile
from django import forms
from django.contrib.auth.models import User
from random import choice
import string
from django_select2 import *
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError


HOSTEL = [('Alakananda',"Alakananda"),('Brahmaputra',"Brahmaputra"),('Cauvery',"Cauvery"),('Ganga',"Ganga"),('Godavari',"Godavari"),('Jamuna',"Jamuna"),('Krishna',"Krishna"),('Mahanadhi',"Mahanadhi"),('Mandakini',"Mandakini"),('Narmada',"Narmada"),('Pampa',"Pampa"),('Saraswathi',"Saraswathi"),('Sarayu',"Sarayu"),('Sharavati',"Sharavati"),('Sindhu',"Sindhu"),('Tamiraparani',"Tamiraparani"),('Tapti',"Tapti")]

TYP = [('Admin','Admin'),('Core','Core'),('Convener','Convener'),('Coordinator','Coordinator')]

# validators

def valid_user_name_create(value):
    username=''
    for i in value.split():
        i=i.lower()+'_'
        username+=i
    username=username[:-1]
    user=User.objects.filter(username=username)
    if user:
        raise ValidationError(u'User already exists')
    else:
        pass

def valid_user_name(value):
    user = User.objects.filter(username=value)
    if len(user)>1:
        raise ValidationError(u'Username already exists')
    else:
        pass

def genpass(length, chars=string.letters + string.digits):
    passwd = ''
    for i in range(length):
        passwd+=choice(chars)
    return passwd

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    username.widget.attrs.update({'class':'form-control','placeholder':'Username'})
    password.widget.attrs.update({'class':'form-control','placeholder':'Password'})

class AddUserForm(forms.ModelForm):
    name = forms.CharField(max_length=100,validators=[valid_user_name_create])
    email = forms.EmailField(help_text='The password will be sent to this email E-mail address')
    hostel = Select2ChoiceField(choices=HOSTEL)
    typ = forms.ChoiceField(choices=TYP)
    class Meta:
        model = UserProfile
        fields = ['name','email','typ','contact_number','hostel']

    def __init__(self,*args,**kwargs):
        super(AddUserForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            if field not in ['hostel']:
                self.fields[field].widget.attrs.update({'class':'form-control'})
            else:
                self.fields[field].widget.attrs.update({'style':'width:300px'})

    def save_user(self):
        userprofile = self.save(commit=False)
        user = User()
        username = ''
        for i in self.cleaned_data['name'].split():
            i=i.lower()+'_'
            username+=i
        username=username[:-1]
        user.username= username
        user.email = self.cleaned_data['email']
        password = genpass(10,string.ascii_letters) 
        user.set_password(password)
        user.save()
        userprofile.user=user
        userprofile.save()
        return password

class EditProfileForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100,validators=[valid_user_name])
    email = forms.EmailField()
    hostel = Select2ChoiceField(choices=HOSTEL)
    
    class Meta:
        model = UserProfile
        fields = ['name','username','email','nick','contact_number','hostel']

    def __init__(self,*args,**kwargs):
        super(EditProfileForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            if field != 'hostel':
                self.fields[field].widget.attrs.update({'class':'form-control'})
        self.fields['name'].initial = self.instance.user.first_name
        self.fields['email'].initial = self.instance.user.email
        self.fields['username'].initial = self.instance.user.username
        self.fields['nick'].initial = self.instance.nick

    def save_profile(self,user):
        userprofile=self.save()
        user = userprofile.user
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['name']
        user.save()
        return True

class ChangePasswordForm(forms.Form):
    password_old = forms.CharField(max_length=100,widget=forms.PasswordInput())
    password_new_1 = forms.CharField(max_length=100,widget=forms.PasswordInput())
    password_new_2 = forms.CharField(max_length=100,widget=forms.PasswordInput())

    def __init__(self,*args,**kwargs):
        super(ChangePasswordForm,self).__init__(*args,**kwargs)
        try:
            for field in self.fields:
                self.fields[field].widget.attrs.update({'class':'form-control'})
                self.fields['password_old'].widget.attrs.update({'placeholder':'Enter old password'})
                self.fields['password_new_1'].widget.attrs.update({'placeholder':'Enter new password'})
                self.fields['password_new_2'].widget.attrs.update({'placeholder':'Confirm new password'})
        except:
            pass
