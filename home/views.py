from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from django.contrib import messages
from .models import User
from django.contrib.auth.hashers import make_password

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
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name,email,phone,content)
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request,"Please Fill the form correctly")
        else:
            contact=Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,"Your issue has been Successfully saved")
    return render(request,"contact.html")
def signin(request):
    return render(request,"signin.html")

def signup(request):
    if request.method == 'POST':
        # Process form submission and create a new user in the database
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Hash the password
        password_hash = make_password(password)

        # Create a new user with the hashed password
        user = User.objects.create(username=username, email=email, password=password_hash)
        user.save()
        # Redirect to the login page or any other appropriate page
        return redirect('login')

    return render(request, 'signup.html')

def login(request):
    error_message = ''  # Initialize the error message variable

    if request.method == 'POST':
        # Retrieve user input from the form
        username = request.POST['username']
        password = request.POST['password']

        # Check if a user with the given username and password exists
        user = User.objects.filter(username=username, password=password).first()

        if user:
            # Successful login, set a session or use Django's authentication system
            # For simplicity, we'll set a session here
            request.session['user_id'] = user.id
            return redirect('dashboard')

        # Invalid credentials, display an error
        error_message = 'Invalid username or password'

    return render(request, 'login.html', {'error_message': error_message})


def dashboard(request):
    # Check if the user is authenticated (you can use Django's authentication system)
    if 'user_id' in request.session:
        return render(request, 'dashboard.html')

    # If not authenticated, redirect to the login page
    return redirect('login')
