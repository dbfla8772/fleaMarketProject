from django.contrib import admin
from django.urls import path, include  
from fleaMarket.views import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('fleaMarket/', include('fleaMarket.urls')), 
    path('account/', include('account.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 