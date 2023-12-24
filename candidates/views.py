from django.shortcuts import render
from .models import CandidateProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def dashboard_home(request):
     return render(request, 'candidate-dashboard.html')

def applied_internships(request):
     return render(request, 'candidate-dashboard-applied-job.html')

def saved_internships(request):
     return render(request, 'candidate-dashboard-shortlisted-resume.html')

@login_required(login_url='signin')
def edit_profile(request):
    user_profile = CandidateProfile.objects.get(user=request.user)

    if request.method == 'POST':

            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            title = request.POST['title']
            location = request.POST['location']
            languages = request.POST['languages']
            university = request.POST['university']
            major = request.POST['major']
            bio = request.POST['bio']
            cgpa = request.POST['cgpa']

            user_profile.first_name = first_name
            user_profile.last_name = last_name
            user_profile.title = title
            user_profile.location = location
            user_profile.languages = languages
            user_profile.university = university
            user_profile.major = major
            user_profile.bio = bio
            user_profile.cgpa = cgpa

            if request.FILES.get('image') == None:
                image = user_profile.profpic
            else:
                image = request.FILES.get('image')
            
            user_profile.profpic = image
            user_profile.save()


    return render(request, 'candidate-dashboard-profile.html', {'user_profile': user_profile})


def view_profile(request, pk):
     user_object = User.objects.get(username=pk)
     user_profile = CandidateProfile.objects.get(user=user_object)
     return render(request, 'candidates-single-v3.html', {'user_profile': user_profile})

def messaging(request):
     return render(request, 'dashboard-messages.html')

def book_interview(request):
     return render(request, 'candidate-dashboard-schedule.html')