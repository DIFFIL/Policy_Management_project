from django.shortcuts import render, HttpResponse

def index(request):
    return render(request,"index.html")
def login(request):
    return render(request,"login.html")
def logout(request):
    return render(request,"login.html")
