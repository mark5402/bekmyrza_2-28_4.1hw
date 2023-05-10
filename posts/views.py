from django.http import HttpResponse
from django.shortcuts import render
from datetime import date, datetime


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello, it is my project! ')


def now_date(request):
    if request.method == 'GET':
        return HttpResponse(datetime.now())


def good_bye(request):
    if request.method == 'GET':
        return HttpResponse('Goodbye maaan!')
