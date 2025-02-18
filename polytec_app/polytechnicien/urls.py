from django.urls import path
from . import views
from .views import homepage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('polytechnicien/<int:member_id>/', views.member_view, name='polytechnicien')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
