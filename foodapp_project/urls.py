from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
urlpatterns =[
    path('admin/', admin.site.urls),
    path('', include('reslist.urls')),
    url(r'^user/',include('User.url')),
    url('',include('foodlist.urls')),
    url(r'^rider/',include('Rider.url')),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
