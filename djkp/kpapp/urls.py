#from django.conf.urls import path
from django.conf.urls import url
from . import views
from kpapp.views import ClassBV
urlpatterns = [
	url(r'^$' , views.first_method , name = 'first_method'),
	url(r'dummy' , views.dummy_method , name = 'dummy_method'),
	url(r'name_form' , views.get_name , name = 'name_form'),
	#url(r'thanks' , views.thanks , name = 'thanks'),
 	url(r'school_list' , views.school_list , name = 'school_list'),
 	url(r'cbv' , ClassBV.as_view() , name = 'cbv'),
 	

 	
]