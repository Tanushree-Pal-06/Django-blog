from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .models import Blog,Category
from django.db.models import Q
# Create your views here.
def posts_by_category(request,pk):
    posts=Blog.objects.filter(status='Published',category=pk)

    try:
     category=Category.objects.get(pk=pk)
    except:
       #redirect to homepage
       return redirect('home') 
    
    # or use
    #category=get_object_or_404(Category,pk=pk)
    context={
        'posts':posts,
        'category':category
    }
    return render(request,'posts_by_category.html',context)

def blogs(request,slug):
   single_blog=get_object_or_404(Blog,slug=slug,status='Published')
   context={
      'single_blog':single_blog
   }
   return render(request,'blogs.html',context)

def search(request):
   keyword=request.GET.get('keyword')
  # i means case insensitive
  # , acts as AND opertor
  # | is Or operator
  # Q is used for ensuirng multiple OR conditions in Django
   blogs=Blog.objects.filter(Q(title_icontains=keyword)| Q(short_decription__icontains=keyword)| Q(blog_body__icontains=keyword),status='Published')
   context={
      'blogs':blogs
   }
   return render(request,'search.html',context)