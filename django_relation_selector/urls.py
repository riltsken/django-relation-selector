from django.conf.urls.defaults import *

urlpatterns = patterns('django_relation_selector.views',
	url('^relation/select/$',	'relation_select',	name='model_relation_select'),
)
