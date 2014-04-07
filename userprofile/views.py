from django.shortcuts import *
try:
    from django.core.serializers.json import simplejson
except:
    import simplejson
import datetime
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, Group
from django.contrib import auth,messages
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.mail import EmailMultiAlternatives,send_mail
from django.core.urlresolvers import reverse

from userprofile.models import UserProfile
from forms import AddUserForm, EditProfileForm, LoginForm, ChangePasswordForm

def login(request):
    if request.method == 'POST':
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            username = loginForm.cleaned_data['username']
            password = loginForm.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is None:
                messages.error(request,'Invalid username or password,Login again')
                return HttpResponseRedirect(reverse('home'))
            else:
                auth.login(request,user)
                messages.success(request,'Successfully logged in')
                return HttpResponseRedirect(reverse('home'))
        else:
            messages.error(request,'Enter valid details</a>')
            return HttpResponseRedirect(reverse('home'))

    else:
        title = "Login"
        user = request.user 
        if not user.is_anonymous():
            messages.info(request,'Already logged in')
            return HttpResponseRedirect(reverse('home'))
        loginForm = LoginForm()
        return_url = reverse('login')
        to_return={
            'form' : loginForm,
            'title' : title,
            'return_url' : return_url,
            'button' : 'Login' ,
        }
        return render(request,'form.html',to_return,context_instance=RequestContext(request))

def logout(request):
    auth.logout(request)
    messages.success(request,'Successfully logged out')
    return HttpResponseRedirect(reverse('home'))

def add_user(request,template_name='form1.html'):
    adduserForm = AddUserForm(request.POST or None)
    if request.method == 'POST':
        if adduserForm.is_valid():
            password = adduserForm.save_user()
            messages.success(request,'User successfully added')
            messages.success(request,password)
            return HttpResponseRedirect(reverse('club_main'))
    if request.user.get_profile().typ == 'Admin':
        adduserForm.fields['typ'].choices = [('Admin','Admin'),('Core','Core'),('Convener','Convener'),('Coordinator','Coordinator')]
    elif request.user.get_profile().typ == 'Core':
        adduserForm.fields['typ'].choices = [('Convener','Convener'),('Coordinator','Coordinator')]
    elif request.user.get_profile().typ == 'Convener':
        adduserForm.fields['typ'].choices = [('Coordinator','Coordinator')]
    return_url = reverse('add_user')
    to_return={
        'form' : adduserForm,
        'title' : "Add User",
        'return_url' : return_url,
        'button' : 'Add',
    }
    return render(request,template_name,to_return)

def edit_profile(request):
    to_return = {}
    userprofile = request.user.get_profile()
    editprofileForm = EditProfileForm(request.POST or None,instance=userprofile)
    for field in editprofileForm.fields:
        print editprofileForm[field].errors
    if editprofileForm.is_valid():
        if editprofileForm.save_profile(request.user):
            messages.success(request,'Successfully updated profile.')
            return HttpResponseRedirect(request.path)
    return_url=reverse('edit_profile')
    to_return = {
        'form' : editprofileForm,
        'title' : 'Edit Profile',
        'return_url' : return_url,
        'button' : 'Update',
    }
    return render(request,'form1.html',to_return,context_instance=RequestContext(request))

def change_password(request):
    if request.method == 'POST':
        changepasswordForm = ChangePasswordForm(request.POST)
        if changepasswordForm.is_valid():
            user = request.user
            password_old = changepasswordForm.cleaned_data['password_old']
            if user.check_password(password_old):
                password_new_1 = changepasswordForm.cleaned_data['password_new_1']
                password_new_2 = changepasswordForm.cleaned_data['password_new_2']
                if password_new_1 == password_new_2:
                    user.set_password(password_new_1)
                    user.save()
                    messages.success(request,'Password successfully changed')
                    return HttpResponseRedirect(request.path)
                else:
                    messages.error(request,'Passwords don\'t match')
                    return HttpResponseRedirect(request.path)
            else:
                messages.error(request,'Wrong password, try again')
            return HttpResponseRedirect(request.path)
        else:
            messages.error(request,'Incorrect entry')
            return HttpResponseRedirect(request.path)
    else:
        editprofileForm = ChangePasswordForm()
        return_url=reverse('change_password')
        to_return = {
            'form' : editprofileForm,
            'title' : 'Change Password',
            'return_url' : return_url,
            'button' : 'Change',
        }
        return render(request,'form.html',to_return,context_instance=RequestContext(request))
