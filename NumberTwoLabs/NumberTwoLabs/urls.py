from django.conf.urls import patterns, include, url
from django.contrib import admin
from pooperRater import views
from django.views.generic import RedirectView





urlpatterns = patterns('',

    url(r'^$', 'pooperRater.views.places', name='places'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.home_page, name='index'),


    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': 'successful_logout'}, name='logout'),
    url(r'^successful_logout/$', 'pooperRater.views.successful_logout', name='successful_logout'),
    url(r'^login_redirect/$', 'pooperRater.views.login_redirect', name='login_redirect'),
    url('', include('django.contrib.auth.urls', namespace='auth')),


    url(r'^api/v1/', include('pooperRater.api.urls')),
    url(r'^yelp/ajax/$', views.yelp_ajax, name='yelp_ajax'),
    url(r'^profile', views.profile, name='profile'),
)
