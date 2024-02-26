from django.shortcuts import render

def mainpage(request):
    return render(request, 'dashboard.html')
# Create your views here.
