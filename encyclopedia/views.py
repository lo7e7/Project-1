from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse
from . import util
from encyclopedia import util
from django.http import HttpResponse,HttpResponseRedirect
import random


#A form to search pages


class NewForm(forms.Form):
    search=forms.CharField(label="")


# A form to create a new page


class CreateForm(forms.Form):
    create_title=forms.CharField(label="Enter Title  ")
    create_content=forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":3}),label="Type your data  ")


# A page to edit form


class EditForm(forms.Form):
    
    edit_title=forms.CharField(label="Enter Title  ")
    edit_body=forms.CharField(label="Edit your page",widget=forms.Textarea(attrs={"rows":3, "cols":3}))
   


# function for website's landing page
def index(request):
    if request.method=="POST":
        srch=NewForm(request.POST)
        if srch.is_valid():
             search=srch.cleaned_data["search"]
             title=search          
             return render(request, "encyclopedia/search.html",{
                "entries": util.list_entries(),
                "title": title.upper()
                 })
             
    else:          
     return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "search":NewForm()
        
         
    })
# function for displaying files
def entry_page(request,name):
    return render(request, "encyclopedia/entry.html",{
        "entrypage" : util.get_entry(name),
        "title": name,
        "search":NewForm()
    })


# function to create a page
def create_page(request):
    if request.method=="POST":
       form=CreateForm(request.POST)
       if form.is_valid():
           create_title=form.cleaned_data["create_title"]
           create_content=form.cleaned_data["create_content"]
           if util.get_entry(create_title):
                return HttpResponse('<h1>Page already exists</h1>')
           else:    
               util.save_entry(create_title,create_content)
               return HttpResponseRedirect(reverse("encylopedia:index"))
             
    return render(request,"encyclopedia/create.html",{
        "forms":CreateForm()
    })


# function to edit page
def edit_pages(request,page_name):
    initial_data={
        'edit_title':page_name,
        'edit_body':util.get_entry(page_name)
        }
    form=EditForm(initial=initial_data)
    if request.method=="POST":    
         if form.is_valid():  
            edit_body=form.cleaned_data["edit_body"]
            util.save_entry(page_name,edit_body)          
            return HttpResponseRedirect(reverse("encylopedia:entry-page"))
         
 
    return render(request,"encyclopedia/edit_page.html",{
             "entrypage" : util.get_entry(page_name),
             "form":form, 
             "title":page_name
           })


#function to randomize page
def random_page(request):
    random_pg=util.list_entries()
    randompg=random.choice(random_pg)
    return render(request, "encyclopedia/entry.html",{
        "entrypage" : util.get_entry(randompg),
        "title": randompg,
        "search":NewForm()
        
    })

