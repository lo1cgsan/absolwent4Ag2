from django.http import HttpResponse

from django.shortcuts import render
from osoby.forms import UserLoginForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse

from osoby.models import Absolwent
from django.contrib.auth.forms import UserCreationForm

def lista_absolwentow(request):
    absolwenci = Absolwent.objects.all()
    kontekst = {'absolwenci': absolwenci}
    return render(request, 'osoby/lista_absolwentow.html', kontekst)

def about(request):
    return HttpResponse("<h1>Informacje o aplikacji</h1>")

def loguj_osobe(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            nazwa = form.cleaned_data['nazwa']
            haslo = form.cleaned_data['haslo']
            user = authenticate(request, username=nazwa, password=haslo)
            if user is not None:
                login(request, user)
                messages.success(request, "Zostałeś zalogowany!")
                return redirect(reverse('osoby:lista'))
            else:
                messages.error(request, "Błędny login lub hasło!")

    else:
        form = UserLoginForm()
    kontekst = {'form': form}
    return render(request, 'osoby/loguj_osobe.html', kontekst)

def wyloguj_osobe(request):
    logout(request)
    messages.info(request, "Zostałeś wylogowany!")
    return redirect(reverse('osoby:lista'))

def rejestruj_osobe(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Utworzono konto! Możesz się zalogować!")
            return redirect(reverse('osoby:loguj-osobe'))
    else:
        form = UserCreationForm()
    return render(request, 'osoby/rejestruj_osobe1.html', {'form': form})
