from django.conf.urls.defaults import patterns, include, url
from aldown import urls as al_urls

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test_django2.views.home', name='home'),
    # url(r'^test_django2/', include('test_django2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^aldown/?',include(al_urls)),
)
