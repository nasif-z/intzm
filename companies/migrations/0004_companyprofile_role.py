# Generated by Django 4.2.6 on 2023-11-07 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_companyprofile_address_companyprofile_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofile',
            name='role',
            field=models.CharField(choices=[('candidate', 'Candidate'), ('company', 'Company')], default='candidate', max_length=20),
        ),
    ]
