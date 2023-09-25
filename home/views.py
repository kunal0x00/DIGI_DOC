from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context ={
        "variable1":"a"
    }
    return render(request,"index.html",context)
def about(request):
    return render(request,"about.html")
def security(request):
    return render(request,"security.html")
def resources(request):
    return render(request,"resources.html")
def contact(request):
    return render(request,"contact.html")
def signin(request):
    return render(request,"signin.html")
def signup(request):
    return render(request,"signup.html")