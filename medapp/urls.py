from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('Resume', views.resume, name='resume'),
    path('Contact/', views.contact, name='contact'),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)
