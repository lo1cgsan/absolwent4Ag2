from django.http import HttpResponse

from django.shortcuts import render
from osoby.forms import UserLoginForm


def lista_absolwentow(request):
    return HttpResponse("<h1>Aplikacja osoby!</h1>")

def about(request):
    return HttpResponse("<h1>Informacje o aplikacji</h1>")

def loguj_osobe(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = UserLoginForm()
    kontekst = {'form': form}
    return render(request, 'osoby/loguj_osobe.html', kontekst)
