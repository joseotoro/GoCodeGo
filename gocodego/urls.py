from django.conf.urls import patterns, include, url
from django.contrib import admin
import views
import go

urlpatterns = patterns('',
    # Admin site
    url(r'^admin/', include(admin.site.urls)),

    # Social auth
    url(r'', include('social_auth.urls')),
    url(r'^logout/', views.logout, name='logout'),

    # Problems
    url(r'^problems/$', views.problems, name='problems'),
    url(r'^search/$', views.search, name='search'),
    url(r'^problems/(\d+)$', views.detail, name='detail'),
    url(r'^problems/check_solution/$', go.check, name='check_solution'),
    url(r'^problems/save_solution/$', go.save, name='save_solution'),

    # Profile
    url(r'^users/$', views.users, name='users'),
    url(r'^profile_edit/$', views.profile_edit, name='profile_edit'),
    url(r'^profile_save/$', views.profile_save, name='profile_save'),
    url(r'^users/(.*)$', views.user, name='profile'),

    # Index
    url(r'^$', views.index, name='index'),
)
