from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
	return render(request, "wordcount/home.html", {"name":"wordcount-site"})

def count(request):
	data = request.GET["fulltextares"]
	data = data.strip().split()
	dic = {}
	for item in data:
		if item in dic:
			dic[item]+=1
		else:
			dic[item]=1
	#dic = dic.items()
	print(dic)
	return render(request, "wordcount/count.html",{"mytext": data, "list": dic.items()})
