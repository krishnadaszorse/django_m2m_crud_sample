from .views import job_list,post_job,update_job,delete_job
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                     
                       url(r'^$', job_list ,name='job_list'),
                       url(r'^job/post/$', post_job ,name='post_job'),
                       url(r'^job/(?P<id>[\d+]+)/update/$', update_job ,name='update_job'),
                       url(r'^job/(?P<id>[\d+]+)/delete/$', delete_job ,name='delete_job'),
                       # url(r'^recover/(?P<signature>.+)/$', recover_done,name='password_reset_sent'),
                       # url(r'^recover/$', recover, name='password_reset_recover'),
                       # url(r'^reset/done/$', reset_done, name='password_reset_done'),
                       # url(r'^reset/(?P<token>[\w:-]+)/$', reset,name='password_reset_reset'),
                  )

