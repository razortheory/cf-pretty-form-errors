from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^/?$', views.ExampleFormView.as_view(), name='example_form'),
)
