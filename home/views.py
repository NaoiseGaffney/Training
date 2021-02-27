from django.shortcuts import render

# Create your views here.


def index(request):
    """
    Index / Home Page for the Project
    """
    return render(request, 'home/index.html')
