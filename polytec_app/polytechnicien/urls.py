from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('polytechnicien/<int:member_id>/', views.member_view, name='polytechnicien'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', views.login_view, name='login'),  # Changed URL pattern
    path('certification/', views.certification, name='certification'),  # Changed URL pattern
    path('home', views.home, name='home'),  # Changed URL pattern
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
