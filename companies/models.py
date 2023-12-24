from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

Company = get_user_model()

class CompanyProfile(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=150, null=True)
    location = models.CharField(max_length=100, null=True)
    website = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=20, null=True)
    company_email = models.CharField(max_length=50, null=True)
    about = models.TextField(null=True)
    primary_industry = models.CharField(max_length=50, null=True)
    company_size = models.CharField(max_length=20, null=True, blank=True)
    founded_year = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)

    ROLES = (('candidate', 'Candidate'), ('company', 'Company'))
    role = models.CharField(
        max_length=20,
        choices=ROLES,
        default='candidate'
    )

    def __str__(self):
        return self.user.company_name
    

class JobPost(models.Model):
    user = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    description = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    allowance = models.IntegerField(default=0)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
