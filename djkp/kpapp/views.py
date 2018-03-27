from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse ,HttpResponseRedirect
from .models import Article , Schools
from django.contrib.auth.models import User
from django.views import View
from .forms import NameForm
from bs4 import BeautifulSoup	
import requests
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
			htm = "<html><head><title>Thanks </title></head><body><center >Thanks </center></body></html>"
			return HttpResponse(htm)
	else:
		form = NameForm()

	return render(request, 'kpapp/name_form.html', {'form': form})