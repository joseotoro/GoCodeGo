from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gocodego.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social_auth.urls')),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^problem/(\d)$', views.detail, name='detail'),
    url(r'^$', views.index, name='index'),
)
