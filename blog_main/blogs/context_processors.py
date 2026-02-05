from .models import Category
#this will pass the categories to all templates 
def get_categories(request):
    categories=Category.objects.all()
    return dict(categories=categories)