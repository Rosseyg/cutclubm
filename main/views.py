from django.shortcuts import render, get_object_or_404, redirect
from .models import Barber, Service
from django.http import HttpResponse
from .forms import UserRegistrationForm

def index(request):
    return HttpResponse("Hello, world. You're at the main index. Welcome to Master Club.  Login to Book")

def barber_list(request):
    barbers = Barber.objects.all()
    return render(request, 'main/barber_list.html', {'barbers': barbers})

def barber_detail(request, pk):
    barber = get_object_or_404(Barber, pk=pk)
    return render(request, 'main/barber_detail.html', {'barber': barber})

def service_list(request):
    services = Service.objects.all()
    return render(request, 'main/service_list.html', {'services': services})

def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'main/service_detail.html', {'service': service})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})