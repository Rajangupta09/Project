from django.shortcuts import render,HttpResponse, get_object_or_404, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login




def login(request):
	if(request.method=="POST"):
		print("ok")
		params=request.POST
		user=authenticate(params['username'], params['password'])
		if(user is not None):
			login(request, User.objects.get(user__username=params['username']))
			return HttpResponse('<h1>worked</h1>')
		else:
			return HttpResponse('<h1>error</h1>')
	else:
		return render(request , 'login/login.html')		


def dashboard(request):
	return render(request , 'login/dashboard.html')	

def category(request):
	if(request.method=="POST"):
		post=Categories()
		post.category=request.POST.get('category')
		post.save()
		categories_list = Categories.objects.all().order_by('-date_created')
		return render(request, 'login/category.html',{'categories':categories_list})  
	else:
		categories_list = Categories.objects.all().order_by('-date_created')
		return render(request, 'login/category.html',{'categories':categories_list}) 


def sub_category(request):
	if(request.method=="POST"):
		post=sub_categories()
		post.sub_category=request.POST.get('sub_category')
		post.category_id=request.POST.get('category_id')
		post.save()
		categories_list = Categories.objects.all().order_by('-date_created')
		sub_categories_list = sub_categories.objects.all().order_by('-date_created')
		return render(request, 'login/sub_category.html',{'categories':categories_list,'sub_categories':sub_categories_list,})  
	else:
		sub_categories_list = sub_categories.objects.all().order_by('-date_created')
		categories_list = Categories.objects.all().order_by('-date_created')
		return render(request, 'login/sub_category.html',{'categories':categories_list,'sub_categories':sub_categories_list,})          

def CategoryDelete(request, pk,):
    cdelete = get_object_or_404(Categories, pk=pk)    
    if request.method=='POST':
        cdelete.delete()
        return redirect('category')
    return render(request, 'login/category.html', {'cdelete': cdelete})

def SubCategoryDelete(request, pk,):
    cdelete = get_object_or_404(sub_categories, pk=pk)    
    if request.method=='POST':
        cdelete.delete()
        return redirect('sub_category')
    return render(request, 'login/sub_category.html', {'cdelete': cdelete})