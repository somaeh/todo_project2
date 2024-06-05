from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserLoginForm
from django.contrib import messages
from django.views import View
from django.views.generic import ListView
from django.contrib.auth import authenticate, login, logout


def user_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['password'], cd['email'])
            messages.success(request, 'user registeration succesfuly', extra_tags='success')
            return redirect('accounts_app:list_user')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts_app/register.html', context={'form': form} )
    
    
    
    
    
    
class ListView(View):
    queryset= None
    template_name = None
    
    def get(self, request):
        return render(request, self.template_name, {'form': self.queryset})  
    
    
class ListUserBaseView(ListView):
    queryset = User.objects.all()
    template_name = "accounts_app/listuser.html" 
    
    
    
# def login_user(request):
#     if request.method == 'POST':
#         form = UserLoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, 'user lpgin successfully', extra_tags='success')
#                 return redirect('accounts_app:list_user')
#             else:
#                 messages.error(request, 'username and password is wrong', extra_tags='danger')
               
        
        
#     else:
#         form = UserLoginForm()
#     return render(request, 'accounts_app/login.html', context={'form': form})

def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have been logged in successfully!', extra_tags='success')
                return redirect('home_app:home')  # هدایت کاربر به صفحه اصلی بعد از ورود
            else:
                messages.error(request, 'Invalid username or password. Please try again.', extra_tags='danger')
    else:
        form = UserLoginForm()
    
    return render(request, 'accounts_app/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'logout user successfully', extra_tags='success')
    return redirect('home_app:home')