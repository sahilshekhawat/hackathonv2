from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('app.views',
    # Examples:
      url(r'^home/user_home/$', 'user_home', name='user_home'),

    # url(r'^$', 'hackathon.views.home', name='home'),
    # url(r'^hackathon/', include('hackathon.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
