from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
                       url(r'^', include('cf_example.urls', namespace='cf_example')),
                       )
