from django.shortcuts import render
from django.http.response import HttpResponse
import datetime as dt
date1=dt.datetime.now()


def dateview(request):

    x="<h1>the current date and time is {}</h1>".format(date1)
    return HttpResponse(x)

# Create your views here.
