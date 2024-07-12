from django.shortcuts import render

# Create your views here.

def Virtualization(request):
    return render(request,"Virtualization.html")
def migrations_page(request):
    return render(request,"migrations_page.html")
def security(request):
    return render(request,"security.html")
def mobility(request):
    return render(request,"mobility.html")
def backup(request):
    return render(request,"backup.html")
def storage(request):
    return render(request,"storage.html")