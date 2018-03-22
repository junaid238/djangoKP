from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Article
from django.contrib.auth.models import User

def first_method(request):
	return HttpResponse("Hello people")
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