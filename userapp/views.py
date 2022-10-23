from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.views import View

# Create your views here.

class LoginView(View):
    def get(self, request):
        return render(request, 'page-user-login.html')

    def post(self, request):
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is None:
            return redirect('/login')
        login(request, user)
        return redirect('/')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/login')

class RegisterView(View):
    def get(self, request):
        return render(request, 'page-user-register.html')

    def post(self, request):
        User.objects.create_user(
            username=request.POST.get('username')
        )
        pass