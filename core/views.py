from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

@require_POST
def apply_job(request):
    if not request.user.is_authenticated:
        # Return JSON response for AJAX requests
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'redirect': True, 'url': '/accounts/login/'})
        else:
            messages.info(request, "Please log in to apply for jobs.")
            return redirect('login')
    
    # If user is authenticated, process the job application
    job_id = request.POST.get('job_id')
    job_title = request.POST.get('job_title', 'this position')
    
    # Here you would typically save the application to a database
    # For now, we'll just show a success message
    messages.success(request, f"Your application for {job_title} has been submitted successfully!")
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'success': True, 'message': f'Your application for {job_title} has been submitted successfully!'})
    else:
        return redirect('home')
