from django.shortcuts import render, redirect
from .models import Profile, Experience, Award
from .forms import ProfileForm

def home(request):
    profiles = Profile.objects.all()
    experiences = Experience.objects.all()
    awards = Award.objects.all()
    context = {
        'profiles': profiles,
        'experiences': experiences,
        'awards': awards,
    }
    return render(request, 'base/home.html', context)

def add_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm()
    return render(request, 'base/add_profile.html', {'form': form})
