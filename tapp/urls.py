from django.conf.urls import patterns, include, url

# from django.contrib import admin
# admin.autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'aut.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    #url(r'^simple/', include('simple.urls')),
    (r'^tw/', include('twython_django_oauth.urls')),
    (r'^logged$', 'aut.views.logged'),
    (r'^dashboard$', 'aut.views.dashboard'),
    (r'^definitions$', 'aut.definitions.view'),
    (r'^users$', 'aut.users.view'),
    (r'^analytics$', 'aut.analytics.view'),

    # tedious pages
    (r'^features$', 'aut.pages.features'),
    (r'^pricing$', 'aut.pages.pricing'),
    (r'^about$', 'aut.pages.about'),

)


urlpatterns += staticfiles_urlpatterns()
#urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)