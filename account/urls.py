from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(
                           regex=r'^login/$',
                           view='django.contrib.auth.views.login',
                           kwargs={'template_name': 'account/login.html'},
                           name='login'
                       ),

                       url(
                           regex=r'^logout/$',
                           view='django.contrib.auth.views.logout',
                           kwargs={'next_page': 'account:login'},
                           name='logout'
                       ),

                       )
