from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from candidates.models import CandidateProfile
from companies.models import CompanyProfile, JobPost

def index(request):
    return render(request, 'index-17.html')

def signup(request):
    if request.method == 'POST':
        role = request.POST['role']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already in use.')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken.')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                user_model = User.objects.get(username=username)
                if role == 'candidate':
                    new_profile = CandidateProfile.objects.create(user=user_model)
                    new_profile.save()
                elif role == 'company':
                    new_profile = CompanyProfile.objects.create(user=user_model)
                    new_profile.save()

                return redirect('edit_profile')

        else:
            messages.info(request, 'Passwords do not match.')
            return redirect('signup')

    else:
        return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard_home')
        else:
            messages.info(request, 'Invalid username or password.')
            return redirect('signin')
    else:
        return render(request, 'login.html')
    
def packages(request):
    return render(request, 'pricing.html')

@login_required(login_url='signin')
def signout(request):
    auth.logout(request)
    return redirect('signin')

def view_post(request, id):
    job = JobPost.objects.get(id=id)
    return render(request, 'job-single-5.html', {'job': job})

def job_feed(request):
    jobs = JobPost.objects.all()
    return render(request, 'job-list-v6.html', {'jobs': jobs})