from django.conf.urls import patterns, url


urlpatterns = patterns('',
                       url(r'^$', 'info.views.home', name='home'),
                       url(r'^view-detail/(?P<detail_id>\d+)/$', 'info.views.view_detail', name='view_detail'),
                       url(r'^detail-list/$', 'info.views.detail_list', name='detail_list'),
                       )
