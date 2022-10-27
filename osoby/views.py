from django.http import HttpResponse

def lista_absolwentow(request):
    return HttpResponse("<h1>Aplikacja osoby!</h1>")

def about(request):
    return HttpResponse("<h1>Informacje o aplikacji</h1>")
