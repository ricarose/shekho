from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'shekho.session.views.index'),
    url(r'^sessions/submit', 'shekho.session.views.submit'),
    url(r'^sessions/browse', 'shekho.session.views.browse'),
    url(r'^sessions/dashboard', 'shekho.session.views.dashboard'),
    url(r'^sessions/view/(?P<session_id>\d+)/$', 'shekho.session.views.details'),
    url(r'^sessions/(?P<session_id>\d+)/signup$', 'shekho.session.views.session_signup'),
    url(r'^sessions/(?P<session_id>\d+)/confirm$', 'shekho.session.views.session_confirm'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'shekho.session.views.user_logout'),
    url(r'^accounts/register/$', 'shekho.session.views.register')

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
