from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .models import Blog,Category
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