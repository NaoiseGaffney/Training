from django.shortcuts import render

# Create your views here.


"""
Single template for the Home / Landing Page.
"""


def index(request):
    """
    Index / Home Page for the Project
    """
    return render(request, 'home/index.html')
