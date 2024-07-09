from django.contrib import admin
from django.urls import path
from innerpages import views

urlpatterns = [
    path("contact",views.contact,name="contact"),
    path("Virtualization",views.Virtualization,name="Virtualization"),
    path("migrations_page",views.migrations_page,name="migrations_page"),
    
    
]