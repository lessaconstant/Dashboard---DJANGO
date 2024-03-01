from django.shortcuts import render

def mainpage(request):
    return render(request, 'mainpage.html')

def dashboards(request):
    return render(request, 'dashboards.html')
# Create your views here.
