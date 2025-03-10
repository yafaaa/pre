from django.shortcuts import render, redirect
from .models import Profile, Experience, Award
from .forms import ProfileForm

def home(request):
    profiles = Profile.objects.all()
    experiences = Experience.objects.all()
    awards = Award.objects.all()
    
    # Sample data
    if not profiles.exists():
        Profile.objects.create(
            name="Mathias Amare",
            bio="Experienced medical doctor with a passion for patient care and medical research.",
            profile_pic="profile_pics/default.jpg",
            contact_info="Email: mathias@example.com\nPhone: +1234567890\nAddress: 123 Medical Street, Health City"
        )
    
    if not experiences.exists():
        Experience.objects.create(
            title="Senior Medical Doctor",
            description="Worked at Health City Hospital, providing top-notch medical care to patients.",
            start_date="2015-01-01",
            end_date="2025-01-01"
        )
        Experience.objects.create(
            title="Medical Researcher",
            description="Conducted groundbreaking research in the field of cardiology.",
            start_date="2010-01-01",
            end_date="2014-12-31"
        )
    
    if not awards.exists():
        Award.objects.create(
            title="Best Doctor Award",
            description="Awarded for outstanding performance in patient care.",
            date="2020-05-01"
        )
        Award.objects.create(
            title="Research Excellence Award",
            description="Recognized for significant contributions to medical research.",
            date="2018-11-15"
        )
    
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
