from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from django.contrib import messages
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login

from .forms import FileUploadForm


from django.core.files.base import ContentFile


from django.views import View

from django.http import HttpResponse

from django.shortcuts import get_object_or_404


from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode


from django.core.files.uploadedfile import SimpleUploadedFile




# Create your views here.
def index(request):
    return render(request,"index.html")
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



def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Hash the password
        password_hash = make_password(password)

        # Check if a file was uploaded
        if 'file' in request.FILES:
            file = request.FILES['file']
        else:
            # If no file was uploaded, you need to provide some default value or handle it as appropriate
            file = SimpleUploadedFile("default.jpg", b'')

        # Create a new user with the hashed password and the file
        user = User.objects.create(username=username, email=email, password=password_hash, file=file)
        user.save()

        messages.success(request, "Successfully registered and logged in")
        return redirect('dashboard')  # Redirect to the dashboard after successful registration

    return render(request, "signup.html")

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's authenticate function to check credentials
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect('dashboard')  # Redirect to the dashboard after successful login
        else:
            messages.error(request, "Invalid credentials, please try again")

    return render(request, "login.html")

from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    # Check if the user is authenticated (you can use Django's authentication system)
    return render(request, 'dashboard.html')

    if 'user_id' in request.session:
        return render(request, 'dashboard.html')

    # If not authenticated, redirect to the login page
    return redirect('login')


def download_encrypted_file(request, file_id):
    encrypted_file = get_object_or_404(User, pk=file_id)

    # Retrieve the encryption key from the database and decode it
    key = b64decode(encrypted_file.key)

    # Check if the key is empty
    if not key:
        # Handle the case where the key is empty
        # You might want to log an error or return an appropriate response
        return HttpResponse("Error: Empty encryption key")

    # Initialize the AES cipher with the key and mode
    cipher = AES.new(key, AES.MODE_EAX)

    # Read the encrypted content from the file
    encrypted_content = encrypted_file.file_encrypted.read()

    # Decrypt the content
    decrypted_content = cipher.decrypt(encrypted_content)

    # Create a response with the decrypted content
    response = HttpResponse(decrypted_content, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{encrypted_file.file.name}"'
    return response

def download_uploaded_file(request, file_id):
    uploaded_file = get_object_or_404(User, pk=file_id)

    # Retrieve the encryption key from the database and decode it
    key = b64decode(uploaded_file.key)

    # Initialize the AES cipher with the key and mode
    cipher = AES.new(key, AES.MODE_EAX)

    # Read the encrypted content from the file
    encrypted_content = uploaded_file.file.read()

    # Decrypt the content
    decrypted_content = cipher.decrypt(encrypted_content)

    # Create a response with the decrypted content
    response = HttpResponse(decrypted_content, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

def delete_file(request, file_id):
    # Retrieve the file instance
    file_instance = get_object_or_404(User, pk=file_id)

    # Delete the file instance
    file_instance.delete()

    # Redirect back to the file list
    return redirect('file_list')

        
class UploadFileView(View):
    template_name = 'dashboard.html'

    def get(self, request, *args, **kwargs):
        files = User.objects.all()
        return render(request, self.template_name, {'files': files})

    def post(self, request, *args, **kwargs):
        uploaded_file = request.FILES.get('file')

        if uploaded_file:
            # Example: Save the file to the database
            User.objects.create(file=uploaded_file)

        return redirect('upload_file')

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=False)

            # Generate and save the encryption key
            key = get_random_bytes(16)
            uploaded_file.key = b64encode(key).decode('utf-8')

            try:
                # Encrypt the file content
                cipher = AES.new(key, AES.MODE_EAX)
                ciphertext, tag = cipher.encrypt_and_digest(uploaded_file.file.read())


                # Save the encrypted content to file_encrypted attribute
                uploaded_file.file_encrypted.save('encrypted_' + uploaded_file.file.name, ContentFile(ciphertext))

                # Save the instance
                uploaded_file.save()

                return redirect('file_list')

            except Exception as e:
                # Handle encryption errors
                print(f"Encryption error: {e}")
                messages.error(request, "Error occurred during encryption. Please try again.")

    else:
        form = FileUploadForm()

    return render(request, 'upload_file.html', {'form': form})

def file_list(request):
    files = User.objects.all()
    return render(request, 'file_list.html', {'files': files})

def dashboard(request):
    encrypted_files = User.objects.all()
    return render(request, 'dashboard.html', {'files': encrypted_files})


def download_file_taneesha(request, file_id):
    encrypted_file = get_object_or_404(User, pk=file_id)

    # Retrieve the encryption key from the database and decode it
    key = b64decode(encrypted_file.key)

    # Check if the key is empty
    if not key:
        return HttpResponse("Error: Empty encryption key")

    # Initialize the AES cipher with the key and mode
    cipher = AES.new(key, AES.MODE_EAX)

    # Read the encrypted content from the file
    encrypted_content = encrypted_file.file_encrypted.read()

    # Decrypt the content
    decrypted_content = cipher.decrypt(encrypted_content)

    # Create a response with the decrypted content
    response = HttpResponse(decrypted_content, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="decrypted_{encrypted_file.file.name}"'
    return response