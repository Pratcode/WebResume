from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('resume', views.resume, name='resume'),
    path('contact/', views.contact, name='contact'),
    path('', views.home, name='home'),

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)
