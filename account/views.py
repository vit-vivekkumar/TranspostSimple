from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages, auth



class RegistrationView(View):
    def get(self, request):
        return render(request, 'account/register.html')

    def post(self, request):

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        context = {
            'fieldValues': request.POST
        }
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Please! Try other Username')
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'Email already Exist')

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 5:
                    messages.error(request, 'Your Password too short')
                    return render(request, 'account/register.html', context)

                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.is_active = True
                user.save()
                messages.success(request, 'Account successfully created!')
                return redirect('login')

        return render(request, 'account/register.html')
    



class LoginView(View):
    def get(self, request):
        return render(request, 'account/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = auth.authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, 'Welcome, ' +
                                     user.username+' you are now logged in')
                    return redirect('home')
                messages.warning(
                    request, 'Account is not active,please check your email')
                return render(request, 'authentication/login.html')
            messages.warning(
                request, 'Invalid credentials,try again')
            return render(request, 'account/login.html')

        messages.warning(
            request, 'Please fill all fields')
        return render(request, 'account/login.html')


class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        messages.success(request, 'You have been logged out')
        return redirect('home')

