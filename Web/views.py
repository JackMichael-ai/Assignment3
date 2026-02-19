from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def home(request):
    return render(request, '404.html')
def terms(request):
    return render(request, 'terms.html')
def privacy(request):
    return render(request, 'privacy.html')
def services(request):
    return render(request, 'service-details.html')
def portfolio(request):
    return render(request, 'portfolio-details.html')
def starter(request):
    return render(request, 'starter-details.html')
def contact_view(request):
    return render(request, 'contact.html')


from django.http import JsonResponse
from django.shortcuts import render


def contactview(request):
    if request.method == 'POST':
        # Get data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Logic to send email or save to database goes here

        # This JSON response tells the template's 'validate.js' to show the success message
        return JsonResponse({'status': 'success'})

    return render(request, 'contact.html')
