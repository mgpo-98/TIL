from django.shortcuts import redirect, render

# from django.contrib.auth.forms import UserCreationForm
from .forms import CusetomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
# from . models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CusetomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    
    else :
        form = CusetomUserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)

def detail(request,pk):
   

    user = get_user_model().objects.get(pk=pk)
    context = {
        'user': user
    }

    return render(request, 'accounts/detail.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # 세션 저장...
            auth_login(request, form.get_user())
            return redirect('articles:index')

    else:
        form = AuthenticationForm()
    context = {
        'form' : form, 
    }
    return render(request, 'accounts/login.html', context)
