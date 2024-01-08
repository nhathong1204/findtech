from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def RegisterView(request):
    if request.user.is_authenticated:
        messages.success(request, "You are already logged in")
        return redirect('account:account')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            new_user = authenticate(email=email, password=password)
            if new_user is not None:
                login(request, new_user)
                return redirect('account:account')
    else:
        form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'userauths/sign-up.html',context)

def LoginView(request):
    if request.user.is_authenticated:
        messages.success(request, "You are already logged in")
        return redirect('account:account')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are already logged in")
            return redirect('account:account')
        
    context = {
        'form': form
    }
    # if request.method == 'POST':
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    #     try:
    #         user = User.objects.get(email=email)
    #         user = authenticate(email=email, password=password)
    #         if user is not None:
    #             login(request, user)
    #             messages.success(request, "You are now logged in")
    #             return redirect('core:index')
    #         else:
    #             messages.warning(request, "Username or password is incorrect")
    #             return redirect('userauths:sign-in')
    #     except:
    #         messages.warning(request, "User does not exist")
    #         return redirect('userauths:sign-in')
        
    return render(request, 'userauths/sign-in.html',context)  


def LogoutView(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('userauths:sign-in')