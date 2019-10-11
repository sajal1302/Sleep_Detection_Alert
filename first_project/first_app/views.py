from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from first_app import forms
from alarm import main
from first_app.forms import UserForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'first_app/base.html')


def final(request):
    main()
    return render(request, 'first_app/final.html')


@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))


def form(request):
    form = forms.FormName()

    if (request.method == 'POST'):
        # form = forms.FormName(data=request.POST)

        return HttpResponseRedirect(reverse('final'))

    else:
        form = forms.FormName()

    return render(request, 'first_app/form.html', {'form': form})


def register(request):
    registered = False

    if (request.method == 'POST'):
        user_form = UserForm(data=request.POST)


        if (user_form.is_valid()):
            user = user_form.save()
            user.set_password(user.password)
            user.save()


            registered = True

        else:
            print (user_form.errors)

    else:
        user_form = UserForm()


    return render(request, 'first_app/registration.html',
                            {'user_form':user_form,
                            'registered':registered})


def user_login(request):

    if (request.method == 'POST'):
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if (user.is_active):
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect('form')
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'first_app/login.html', {})