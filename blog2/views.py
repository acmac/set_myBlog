# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

from .import models

def index(request):
    articles =models.Aritle.objects.all()
    return render(request,'blog/index.html',{'articles': articles})
