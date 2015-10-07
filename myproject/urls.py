from django.conf.urls import patterns, include, url
from django.http import HttpResponse


urlpatterns = patterns('',
	(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\n", mimetype="text/plain")),
    url(r'^$', 'hello.views.index'),
    #url(r'^page', 'hello.views.page'),
)




