from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate, logout

from .forms import RegisterForm, LoginForm


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('account:login')
        return HttpResponse('Invalid form!!!')
    form = RegisterForm()

    context = {
        'form': form
    }
    return render(request, 'account/register_user.html', context)


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)


