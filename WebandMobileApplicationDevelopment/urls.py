"""WebandMobileApplicationDevelopment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin

# urlpatterns = [
#    url(r'^admin/', include(admin.site.urls)),
# urlpatterns = [url(r'^admin/', include(admin.site.urls)),]

urlpatterns = patterns('',
                url(r'^admin/', include(admin.site.urls)),
                url(r'^$', 'tripplanner.views.home',name='home'),

                # send POST request

                url(r'^your-search/', 'tripplanner.views.get_name',name='get_name'),


                url(r'^login/', 'tripplanner.views.get_login',name='login'),
                url(r'^success-login/', 'tripplanner.views.success_login',name='success_login'),

                url(r'^registration/', 'tripplanner.views.get_registration',name='registration'),
                url(r'^success-registration/', 'tripplanner.views.success_registration',name='success_registration'),

                url(r'^userprofile/', 'tripplanner.views.get_userprofile',name='userprofile'),
                url(r'^logout/','tripplanner.views.logout',name='home'))

