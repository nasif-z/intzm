from django.shortcuts import render, redirect
from .models import CompanyProfile, JobPost
from django.contrib.auth.decorators import login_required

def company_signup(request):
    if request.method == 'POST':
        pass
    else:
        pass

    return render(request, 'dashboard-company-profile.html')

def company_profile_view(request):
    return render(request, 'employers-single-v1.html')

@login_required(login_url='signin')
def create_post(request):
    if request.method == "POST":
        user = request.user.username
        title = request.POST['title']
        description = request.POST['description']
        allowance = request.POST['allowance']
        location = request.POST['location']

        new_post = JobPost.objects.create(
            user=user, 
            title=title, 
            description=description, 
            allowance=allowance,
            location=location
            )
        new_post.save()
        return redirect('create_post')

    else:
        return render(request, 'dashboard-post-job.html')