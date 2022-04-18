from django.shortcuts import get_object_or_404, render
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Neighborhood, Profile,Business,Location,Category,Post
from .forms import BusinessForm, ProfileForm, NeighborhoodForm,PostForm 
# Create your views here.

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'main/profile.html', {"form":form,'profile':profile})

    
def index(request):
    posts = Post.objects.all().order_by("-id")
    return render(request, 'main/index.html', {'posts': posts})

