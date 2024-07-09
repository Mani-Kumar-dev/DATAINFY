from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request,"contact.html")
def Virtualization(request):
    return render(request,"Virtualization.html")
def migrations_page(request):
    return render(request,"migrations_page.html")