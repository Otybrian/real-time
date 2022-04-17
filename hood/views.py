from django.shortcuts import render

# Create your views here.
def index(request):
    welcome='Welcome to my Hood'
    return render(request, 'index.html', {'welcome':welcome})