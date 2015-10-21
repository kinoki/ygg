from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views as rest_views


urlpatterns = patterns('',
                       url(r'^obtain-auth-token/', rest_views.obtain_auth_token),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^info/', include('info.urls', namespace='info')),
                       url(r'^account/', include('account.urls', namespace='account')),
                       )

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
