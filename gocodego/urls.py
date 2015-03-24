from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

urlpatterns = patterns('',
    # Admin site
    url(r'^admin/', include(admin.site.urls)),

    # Social auth
    url(r'', include('social_auth.urls')),
    url(r'^logout/', views.logout, name='logout'),

    # Problems
    url(r'^problems/$', views.problems, name='problems'),
    url(r'^problems/(\d)$', views.detail, name='detail'),

    # Profile
    url(r'^profile/$', views.profile, name='profile'),

    # Index
    url(r'^$', views.index, name='index'),
)
