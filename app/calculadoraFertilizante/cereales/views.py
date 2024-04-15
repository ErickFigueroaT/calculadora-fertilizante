from django.shortcuts import render

def hola(request):
    return render(request,'hola.html')