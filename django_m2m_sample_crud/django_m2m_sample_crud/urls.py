from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_m2m_sample_crud.views.home', name='home'),
    url(r'^', include('job.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
