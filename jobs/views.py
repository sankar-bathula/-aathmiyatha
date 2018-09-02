# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Jobs
# Create your views here.

def home(request):
	return render(request, 'jobs/home.html')


