from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hydjobs(request):
    s='<h1>Hyderabad Jobs Information</h1>'
    return HttpResponse(s)

def punejobs(request):
    s='<h1>Pune Jobs Information</h1>'
    return HttpResponse(s)

def mumbaijobs(request):
    s='<h1>Mumbai Jobs Information</h1>'
    return HttpResponse(s)


def chennaijobs(request):
    s='<h1>Chennai Jobs Information</h1>'
    return HttpResponse(s)
