from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def loginfunction(request):
    return render(request,'login.html')
def gridfunction(request):
    return render(request,'grid.html')
def pagefunction(request):
    return render(request,'page.html')
