#from django.conf.urls import path
from django.conf.urls import url
from . import views
from kpapp.views import ClassBV , ArticleListview
urlpatterns = [
	# url(r'^$' , views.first_method , name = 'first_method'),
	url(r'^$' , views.schema_view ),
	url(r'dummy' , views.dummy_method , name = 'dummy_method'),
	url(r'name_form' , views.get_name , name = 'name_form'),
	url(r'^single_article/(?P<pk>\d+)/$', views.single_article, name='single_article'),
	url(r'school_list' , views.school_list , name = 'school_list'),
	url(r'cbv' , ClassBV.as_view() , name = 'cbv'),
	url(r'^add_new/$', views.add_new, name='add_new'),
	url(r'^demo/$', views.demo, name='demo'),
	url(r'^listview/$', ArticleListview.as_view(), name='listview'),

]