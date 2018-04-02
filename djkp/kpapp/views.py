from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse ,HttpResponseRedirect
from .models import Article , Schools ,Student_obj
from django.contrib.auth.models import User
from django.views import View
from .forms import NameForm 
from bs4 import BeautifulSoup	
import requests
from .forms import ArticleForm
from .forms import DemoForm
from django.utils import timezone
from rest_framework_swagger.views import get_swagger_view

from django.views.generic.list import ListView


schema_view = get_swagger_view(title='DigitalLync API')


def first_method(request):
	# return HttpResponse("Hello people")
	url = "https://www.forbes.com/sites/danielnewman/2018/01/16/top-18-tech-trends-at-ces-2018/#4dfeb833452f"
	page = requests.get(url)
	slashparts = url.split('/')
	content = page.content
	soup = BeautifulSoup(page.content, 'html.parser')
	print(soup.prettify())
	list(soup.children)
	soup.find_all('strong')[1].get_text()
	item_list = soup.find_all('strong')
	len(item_list)
	print("Data From : " +slashparts[2])
	data = []
	for i in range(1 , len(soup.find_all('strong'))):
		ans = soup.find_all('strong')[i].get_text()
		data.append(ans)
		print(ans) 
		htm = "<html><head><title>{{ans }}</title></head><body><center >{{ans}} </center></body></html>"
	return render(request , 'kpapp/schools.html' , {"data" : data})


def dummy_method(request):
	
	articles =  Article.objects.all()
	users = User.objects.all()
	# ans = []
	# for article in articles:
	# 	ans.append(Article.ob jects.get(author_id=1))
	return render(request , 'kpapp/first.html' , {"users" : users, "articles" : articles})
def single_article(request , pk):
	singlePost = Article.objects.get(pk=pk)
	return render(request , 'kpapp/single_article.html' , {"singlePost" : singlePost})
def school_list(request):
	schools = Schools.objects.all()
	return render(request , 'kpapp/schools.html' , {"schools" : schools})

# def thanks(request):
# 	htm = "<html><head><title>Thanks </title></head><body><center >Thanks </center></body></html>"
# 	return HttpResponse(htm)
class ClassBV(View):
	def get(self,request):
		self.stmt = 'hai hello'
		return HttpResponse(self.stmt)

def get_name(request):
	
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			student = form.save(commit=False)
			student.save()

			htm = "<html><head><title>Thanks </title></head><body><center >Thanks </center></body></html>"
			return HttpResponse(htm)
		else:
			return HttpResponse("wrong")	
	else:
		form = NameForm()

	return render(request, 'kpapp/name_form.html', {'form': form})

def add_new(request):
	if request.method == "POST":
		form = ArticleForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return HttpResponse('Thanks for posting')
	else:
		form = ArticleForm()
	return render(request, 'kpapp/add_article.html', {'form': form})

def demo(request):
	if request.method == "POST":
		form = DemoForm(request.POST)
		if form.is_valid():
			emp = form.save(commit=False)
			
			return HttpResponse('Thanks for posting')

	else:
		form = DemoForm()
	return render(request, 'kpapp/employee.html', {'form': form})

class ArticleListview(ListView):
	# def __init__(self, arg):
	# 	super(Listview, self).__init__()
	# 	self.arg = arg
	model = Article

		
