from django.shortcuts import render

# Create your views here.
def jobs(request):
    """
    Render the jobs page.
    """
    return render(request, 'jobs/jobs.html')