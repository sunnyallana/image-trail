from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            # If the submitted data is valid, the user gets authenticated against the database using the authenticate() method.

            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:

                '''
                If the user is successfully authenticated, the user status is checked by accessing the is_active 
                attribute. This is an attribute of Django’s User model. If the user is not active, an HttpResponse 
                is returned with a Disabled account message
                '''

                if user.is_active: 
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})