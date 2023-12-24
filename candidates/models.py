from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class CandidateProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    profpic = models.ImageField(upload_to='profile_pictures', default='blank_profile_picture.png')
    resume = models.FileField(upload_to='resumes', blank=True, null=True)
    title = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    bio = models.TextField(null=True)
    languages = models.TextField(blank=True, null=True)
    university = models.CharField(max_length=200, null=True)
    major = models.CharField(max_length=200, null=True)
    cgpa = models.DecimalField(decimal_places=2, max_digits=3, blank=True, null=True)

    ROLES = (('candidate', 'Candidate'), ('company', 'Company'))
    role = models.CharField(
        max_length=20,
        choices=ROLES,
        default='candidate'
    )

    def __str__(self):
        return self.user.username