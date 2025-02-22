from django.shortcuts import render

# Create your views here.

def index(request):
    """ view to return index page """
    
    return render(request, 'home/index.html')

def about(request):
    """ view to return about us page """
    
    return render(request, 'home/about.html')

def privacy(request):
    """ view to return privacy notice page """
    
    return render(request, 'home/privacy.html')