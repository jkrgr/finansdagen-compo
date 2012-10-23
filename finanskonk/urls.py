from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'compo.views.join_compo_view', name='join'),
	url(r'^start_compo/', 'compo.views.compo_start'),
	url(r'^end_compo/', 'compo.views.compo_end'),
	url(r'^initial_data/', 'compo.views.populate_initial_list'),
    # url(r'^finanskonk/', include('finanskonk.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
