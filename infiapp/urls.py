
from django.urls import path
from infiapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # path("",views.home,name="home"),
    path("",views.index,name="index"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

