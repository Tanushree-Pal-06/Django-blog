from django.db import models
from django.contrib.auth.models import User

#Category Model
class Category(models.Model):
    category_name=models.CharField(max_length=50,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
     
    #django automatically adds 's' at end of every model name in admin so , to rename the incorrect spelling, we can:
    class Meta:
        verbose_name_plural='categories'
    
    def __str__(self):
        return self.category_name

STATUS_CHOICES=(
    ("Draft","Draft"),
    ("Published","Published")
)

#Blog Model
class Blog(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=150,unique=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    featured_image=models.ImageField(upload_to='uploads/%Y/%m/%d')
    short_description=models.TextField(max_length=500)
    blog_body=models.TextField(max_length=2000)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default="Draft")
    is_featured=models.BooleanField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

# About us model
class About(models.Model):
    about_heading=models.CharField(max_length=25)
    about_description=models.TextField(max_length=255)
    
    class Meta:
        verbose_name_plural='about'

    def __str__(self):
        return self.about_heading
    

#follow us model
class SocialLink(models.Model):
    platform=models.CharField(max_length=25)   
    link=models.URLField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.platform
    
    
class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE) # if user gets deleted the comment should also get deleted
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)# if blog deletes, comment also gets deleted
    comment=models.TextField(max_length=250)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
