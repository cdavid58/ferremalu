from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('user.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^invoice_fe/', include('fe.urls')),
    url(r'^invoice_pos/', include('pos.urls')),
    url(r'^client/', include('client.urls')),
    url(r'^inventory/', include('inventory.urls')),
    url(r'^shopping/', include('shopping.urls')),
    url(r'^payroll/', include('payroll.urls')),
    url(r'^report/', include('reports.urls')),
    url(r'^wallet/', include('wallet.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)