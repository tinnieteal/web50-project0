from django.shortcuts import render

from encyclopedia import util
from django import forms 

def entry(request, title):
	entries = util.list_entries()

	if title in entries:
		details = util.get_entry(title, tohtml=True)
		return render(request, "wiki/entry.html", {"title": title, "details": details})
	else:
		return render(request, "encyclopedia/error.html", {"error_message": f"The entry {title} is not found."})



def edit(request, title):
	details = util.get_entry(title, tohtml=False)
	return render(request, "wiki/edit.html", {"title": title, "details": details})


