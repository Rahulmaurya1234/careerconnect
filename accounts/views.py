from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import CustomUserRegistrationForm  # if you're using a form later

CustomUser = get_user_model()

def login_view(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('email')
        password = request.POST.get('password')

        # Since USERNAME_FIELD is 'email', authenticate with email
        user = authenticate(request, username=username_or_email, password=password)
        
        # If authentication with email fails, try to find user by username and authenticate with email
        if not user:
            try:
                # Try to find user by username and get their email
                user_obj = CustomUser.objects.get(username=username_or_email)
                user = authenticate(request, username=user_obj.email, password=password)
            except CustomUser.DoesNotExist:
                # Try to find user by email directly
                try:
                    user_obj = CustomUser.objects.get(email=username_or_email)
                    user = authenticate(request, username=user_obj.email, password=password)
                except CustomUser.DoesNotExist:
                    user = None

        if user:
            login(request, user)
            return redirect('home')  # Make sure 'home' is defined in urls
        else:
            messages.error(request, "You don't have any account with these credentials. Please check your email/username and password or register a new account.")

    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        user_type = request.POST.get('user_type')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'accounts/register.html')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return render(request, 'accounts/register.html')

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return render(request, 'accounts/register.html')

        # Create and save the user
        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            user_type=user_type  # assuming you have this field in your custom user model
        )
        user.save()

        # Automatically log in the user after registration
        login(request, user)
        messages.success(request, "Account created successfully! Welcome to CareerConnect!")
        return redirect('home')

    return render(request, 'accounts/register.html')


def logout_view(request):
    """Comprehensive logout view that handles GET and POST requests"""
    # Handle both GET and POST requests
    if request.method in ['GET', 'POST']:
        try:
            # Check if user is actually logged in
            if request.user.is_authenticated:
                logout(request)
                messages.success(request, "You have been logged out successfully.")
            else:
                messages.info(request, "You were not logged in.")
        except Exception as e:
            messages.error(request, f"Logout error: {str(e)}")
    
    # Always redirect to home page
    return HttpResponseRedirect(reverse('home'))


def profile_view(request):
    """Display user profile page"""
    if not request.user.is_authenticated:
        messages.error(request, "Please log in to access your profile.")
        return redirect('login')
    
    return render(request, 'profilename/profilename.html')
