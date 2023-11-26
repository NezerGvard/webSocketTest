from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_exempt
from django.views import View

from .models import *
from .forms import *

class Music(View):
    def get(self, request):
        return render(request, 'main.html')