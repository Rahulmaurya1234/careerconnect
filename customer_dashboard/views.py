from django.shortcuts import render

# Create your views here.
def customer_dashboard(request):
    """
    Render the customer dashboard page.
    """
    return render(request, 'profilename/profilename.html')  # Adjust the template path as needed