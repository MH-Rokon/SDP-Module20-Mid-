from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, update_session_auth_hash,logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import forms
from . import models
from posts.models import Car,Profile
def register(request):
    if request.method == 'POST':
        registerform = forms.Registerform(request.POST)
        if registerform.is_valid():
            registerform.save()
            messages.success(request, 'Registered Successfully')
            return redirect("profile")
    else:
        registerform = forms.Registerform()
    
    return render(request, 'register.html', {'form': registerform, 'type': 'Register'})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                messages.success(request, 'Logged in Successfully')
                login(request, user)
                return redirect('profile')
            else:
                messages.warning(request, 'Login informtion incorrect')
                return redirect('register')
    else:
        form = AuthenticationForm()
        return render(request, 'register.html', {'form' : form, 'type' : 'Login'})

@login_required            
def updateprofile(request):
    if request.method == 'POST':
        profileform = forms.ChangeUserData(request.POST, instance=request.user)
        if profileform.is_valid():
            profileform.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect("profile")
    else:
        profileform = forms.ChangeUserData(instance=request.user)

    return render(request, 'updateprofile.html', {'form': profileform, 'type': 'UpdateProfile'})
@login_required
def change_password(request):
    if request.method == 'POST':
        change_passwordform = PasswordChangeForm(user=request.user, data=request.POST)
        if change_passwordform.is_valid():
            user = change_passwordform.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Password changed successfully')
            return redirect("profile")
    else:
        change_passwordform = PasswordChangeForm(user=request.user)

    return render(request, 'changepass.html', {'form': change_passwordform, 'type': 'ChangePassword'})





@login_required
def profile(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user)
    saved_cars = user_profile.saved_cars.all()
    return render(request, 'profile.html', {'data': saved_cars, 'type': 'Profile'})


def user_logout(request):
    logout(request)
    messages.success(request, 'Logout  successfully')
    return redirect('login')

