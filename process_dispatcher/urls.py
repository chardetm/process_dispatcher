from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'process_registry.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^pdapp/', include('pdapp.urls')),
    url(r'^demo/', include('demo.urls')),
    url(r'^', include('pdapp.urls')),
]
