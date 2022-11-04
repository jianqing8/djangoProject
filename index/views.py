from django.shortcuts import render


# Create your views here.

def index(request):
    value = 'this is index!'
    print(value)
    return render(request, 'index.html')
