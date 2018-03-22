#from django.conf.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$' , views.first_method , name = 'first_method'),
	url(r'dummy' , views.dummy_method , name = 'dummy_method'),
	url(r'^single_article/(?P<pk>\d+)/$' ,views.single_article , name = 'single_article'	)
]