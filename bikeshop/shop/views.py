from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .models import Bike, Customer, Sale
from .forms import CustomUserCreationForm, BikeForm, CustomerForm, SaleForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'shop/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'shop/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'shop/logout.html'

@login_required
def bike_list(request):
    bikes = Bike.objects.all()
    return render(request, 'shop/bike_list.html', {'bikes': bikes})

@login_required
def bike_add(request):
    if request.method == 'POST':
        form = BikeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bike_list')
    else:
        form = BikeForm()
    return render(request, 'shop/bike_form.html', {'form': form})

@login_required
def bike_edit(request, pk):
    bike = get_object_or_404(Bike, pk=pk)
    if request.method == 'POST':
        form = BikeForm(request.POST, instance=bike)
        if form.is_valid():
            form.save()
            return redirect('bike_list')
    else:
        form = BikeForm(instance=bike)
    return render(request, 'shop/bike_form.html', {'form': form})

@login_required
def bike_delete(request, pk):
    bike = get_object_or_404(Bike, pk=pk)
    if request.method == 'POST':
        bike.delete()
        return redirect('bike_list')
    return render(request, 'shop/bike_confirm_delete.html', {'bike': bike})

# Repeat similar views for Customer and Sale models

