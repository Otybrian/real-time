from django.shortcuts import get_object_or_404, render
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Neighborhood, Profile,Business,Location,Category,Post

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by("-id")
    return render(request, 'main/index.html', {'posts': posts})

