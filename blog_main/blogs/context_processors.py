from .models import Category,SocialLink
#this will pass the categories to all templates 
def get_categories(request):
    categories=Category.objects.all()
    return dict(categories=categories)

def get_social_links(request):
    social_links=SocialLink.objects.all()
    return dict(social_links=social_links)