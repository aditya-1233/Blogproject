from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request,'demoapp/base.html')
def home(request):
    return render(request,'demoapp/Home.html')
def news(request):
    return render(request,'demoapp/news.html')
def politics(request):
    return render(request,'demoapp/politics.html')
def sports(request):
    return render(request,'demoapp/sports.html')
