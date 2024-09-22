
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path
from django.conf.urls.static import static 
from django.conf import settings
from django.urls import path, include
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('kurslar/', include('courses.urls')),
    path('', include('pages.urls')), 
    path('account/', include('account.urls')),
    path('summernote/', include('django_summernote.urls')),



] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static (settings.STATIC_URL, document_root = settings.STATIC_ROOT)   #bu ekleme static dosyaların dışarıdan erişilebilir olması için yapıldı


if settings.DEBUG: #summernote2
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    