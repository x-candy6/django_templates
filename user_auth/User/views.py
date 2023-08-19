from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from . import forms

# Create your views here.


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            retVals = {
                'username': username,
                'password': password,
                'error': True,
                'modalTitle': 'Invalid Login',
                'modalText': 'The username and password combination that you entered was invalid. Please try again. If this continues, please contact support by clicking the "Contact Us" link at the bottom of the page.',
                'modalBtnText': "Close",
                'modalImmediate': True
            }
            return render(request, 'User/login.html', retVals)

    context = {}
    return render(request, 'User/login.html')




def logoutPage(request):
    # The following also clears session data
    logout(request)
    return redirect('home')

def registrationPage(request):
    # print(request.session.session_key)
    # print(request.session['visitorIP'])
    user_form = forms.userRegistrationForm()
    if request.method == 'POST':
        # Prepare the session and the forms.
        user_form = forms.userRegistrationForm(request.POST)
        # Check for Validation errors and send them back to the page
        if not user_form.is_valid():
            print(user_form.errors)
            return render(request, 'User/register.html', {'user_form': user_form,  'feedback': "Error", 'error': user_form.errors})
        else:
            # Save the user, the account, and log in the new user
            user = user_form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # trying to figure out how to put the next 3 lines above 'if user is not None'


                return render(request, "global/home.html", {})
            else:
                # There was an error authenticating the newly registered user.
                return render(request, "User/invalidLogin.html")
    # If just a GET request, then send them the html.
    return render(request, 'User/register.html', {'user_form': user_form})
