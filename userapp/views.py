from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.views import View

from .models import *

from django.core.mail import send_mail
from django.conf import settings

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
        if request.POST.get('p1') != request.POST.get('p2'):
            return redirect('/signup')
        user = User.objects.create_user(
            username=request.POST.get('email'),
            email=request.POST.get('email'),
            password=request.POST.get('p1'),
            first_name=request.POST.get('f'),
            last_name=request.POST.get('l'),
        )
        Profile.objects.create(
            city=request.POST.get('city'),
            phone=request.POST.get('phone'),
            gender=request.POST.get('gender'),
            user = user
        )
        send_mail(
            subject='Confirmation',
            message='To complete your verification please go to this Link',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=True)
        return redirect("/login")