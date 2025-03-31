from django.shortcuts import render
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def blog(request):
    return render(request, 'blog.html')

def testmonials(request):
    return render(request, 'testmonials.html')
    
def register(request):
    return render(request, 'register.html')
# Create your views here.
