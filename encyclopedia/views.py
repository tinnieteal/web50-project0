from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from . import util
import random

# class SearchForm(forms.Form):
#     search_query = forms.CharField(label="q")

def find_related(query):
	entries = util.list_entries()
	res = [] 
	for entry in entries: 
		if query in entry: 
			res.append(entry) 
	return res

def index(request): 
	if request.method == "GET":
		query = request.GET.get('q', default=None)
		if query:
			entries = util.list_entries()
			if query in entries:
				return HttpResponseRedirect("wiki/"+query)
			else:
				related_entries = find_related(query)
				if len(related_entries) != 0:
					return render(request, "encyclopedia/searchresult.html", {
						"entries": related_entries
				})
				else: 
					return render(request, "encyclopedia/error.html", {"error_message": f"Query {query} not found" } )

		else:
			return render(request, "encyclopedia/index.html", {
			    "entries": util.list_entries()
			})

class EntryForm(forms.Form):
    title = forms.CharField(label="title")
    details = forms.CharField(label="details")

def createpage(request):
	if request.method == "GET":
		return render(request, "encyclopedia/create.html")
	elif request.method == "POST":
		form = EntryForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data['title']
			details = form.cleaned_data['details']
			entries = util.list_entries()
			if title not in entries:
				util.save_entry(title, details)
				return HttpResponseRedirect("/wiki/"+title)
			else:
				return render(request, "encyclopedia/error.html", {"error_message": f"Title {title} already exists" })
		else:
			return render(request, "encyclopedia/error.html", {"error_message": "Please enter valid title and content"})



def editpage(request):
	if request.method == "POST":
		form = EntryForm(request.POST)
		print(form.is_valid(), form.errors.as_json())
		if form.is_valid():
			title = form.cleaned_data['title']
			details = form.cleaned_data['details']
			util.save_entry(title, details)
			return HttpResponseRedirect("/wiki/"+title)
		else:
			return render(request, "encyclopedia/error.html", {"error_message": "Please enter valid title and content"})


def randompage(request):
	entries = util.list_entries()
	random_entry = random.choice(entries)
	return HttpResponseRedirect("/wiki/"+random_entry)










