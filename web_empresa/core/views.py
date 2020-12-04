from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

def services(request):
    return render(request,"services.html")

def visit(request):
    return render(request,"visit.html")

def blog(request):
    return render(request,"blog.html")

def contact(request):
    return render(request,"contact.html")

def history(request):
    return render(request,"history.html")

def other(request):
    return render(request,"other.html")
