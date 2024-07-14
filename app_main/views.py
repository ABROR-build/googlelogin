from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views import View


class Home(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'main/home.html')
        else:
            return redirect('Login')
