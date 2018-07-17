# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.shortcuts import render
from blog.models import BlogsPost
from django.http import HttpResponse
# Create your views here.

def blog_index(request) :
    blog_list = BlogsPost.objects.all()
    return render (request,'index.html',{'blog_list':blog_list})

def current_datetime(request) :
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


