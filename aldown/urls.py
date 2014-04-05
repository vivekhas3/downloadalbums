from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fb.views.home', name='home'),
    # url(r'^fb/', include('fb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^/?$','aldown.views.home'),
    (r'^download/(.*)/','aldown.views.download'),
    (r'^aldown_post/$','aldown.views.home_post'),    
)
