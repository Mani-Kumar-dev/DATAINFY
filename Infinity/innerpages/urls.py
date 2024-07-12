from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from innerpages import views

urlpatterns = [
    path("Virtualization",views.Virtualization,name="Virtualization"),
    path("migrations_page",views.migrations_page,name="migrations_page"),
    
    path("security",views.security,name="security"),
    path("mobility",views.mobility,name="mobility"),
    path("storage",views.storage,name="storage"),
    path("backup",views.backup,name="backup"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
