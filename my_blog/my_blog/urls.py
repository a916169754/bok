from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', 'article.views.home'),
    #url(r'^(?P<my_args>\d+)/$', 'article.views.detail', name='detail'),
    #url(r'^test/$', 'article.views.test'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'article.views.home', name='home'),
    url(r'^(?P<id>\d+)/$', 'article.views.detail', name='detail'),
    url(r'^archives/$', 'article.views.archives', name = 'archives'),
    url(r'^tag(?P<tag>\w+)/$', 'article.views.search_tag', name = 'search_tag'),
    url(r'^search/$','article.views.blog_search', name = 'search'),
    url(r'^(?P<cry>\w+)/$', 'article.views.contos', name='biji'),
)
