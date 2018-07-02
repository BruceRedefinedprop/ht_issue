from django.shortcuts import render

"""
The index page is harry tool's launch page.  It includes welcoming
overview and navigation to other elements of the site.

"""

# Create your views here.
def index(request):
    """A view that displays the index page"""
    return render(request, "home/index.html")