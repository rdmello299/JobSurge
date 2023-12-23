# Generated by Django 3.1.4 on 2023-10-14 08:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Job_type', models.CharField(choices=[('ELECTRICAL', 'Electrical'), ('PLUMBING', 'Plumbing'), ('HANDYMAN', 'Handyman')], default=(('ELECTRICAL', 'Electrical'), ('PLUMBING', 'Plumbing'), ('HANDYMAN', 'Handyman')), max_length=50)),
                ('Description', models.CharField(blank=True, max_length=500)),
                ('Date', models.DateField(default='2023-10-14', verbose_name='Required Date')),
                ('Time', models.TimeField(default=datetime.datetime.now, verbose_name='Required Time')),
                ('Priority', models.CharField(choices=[('URGENT', 'Urgent'), ('MODERATE', 'Moderate')], default='URGENT', max_length=10)),
                ('Amount', models.DecimalField(decimal_places=0, default=50, max_digits=6)),
                ('Currency', models.CharField(default='USD', max_length=15)),
                ('Technician_experience_preference', models.IntegerField(default=0)),
                ('Licence', models.BooleanField(default=False, verbose_name='Licence')),
                ('Status', models.CharField(choices=[('OPEN', 'Open'), ('PENDING', 'Pending'), ('CLOSED', 'Closed')], default='OPEN', max_length=50)),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Customer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quote', models.TextField(max_length=1000)),
                ('Date', models.DateField(default='2023-10-14', verbose_name='Date')),
                ('Time', models.TimeField(default=datetime.datetime.now, verbose_name='Time')),
                ('Amount', models.DecimalField(decimal_places=0, default=50, max_digits=6)),
                ('Currency', models.CharField(default='USD', max_length=15)),
                ('Job', models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, related_name='Job', to='advertisement.job')),
                ('Technician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='RequestTechnician', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SavedAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Line1', models.CharField(default='line 1', max_length=80)),
                ('Line2', models.CharField(blank=True, default='line 2', max_length=80)),
                ('City', models.CharField(default='city', max_length=80)),
                ('State', models.CharField(default='state', max_length=80)),
                ('Country', models.CharField(default='country', max_length=80)),
                ('Zipcode', models.IntegerField(default=0)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='savedAddress', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comment', models.TextField(blank=True, max_length=100, null=True)),
                ('Rating', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='Rating')),
                ('Appointment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviewed_appointment', to='advertisement.appointment')),
                ('Reviewee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reviewee', to=settings.AUTH_USER_MODEL)),
                ('Reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reviewer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Message', models.TextField(max_length=1000, null=True)),
                ('Response', models.CharField(choices=[('ACCEPT', 'Accept'), ('REJECT', 'Reject')], default=(('ACCEPT', 'Accept'), ('REJECT', 'Reject')), max_length=50)),
                ('Date', models.DateField(default='2023-10-14', verbose_name='Date')),
                ('Time', models.TimeField(default=datetime.datetime.now, verbose_name='Time')),
                ('Amount', models.DecimalField(decimal_places=0, default=50, max_digits=6)),
                ('Currency', models.CharField(default='USD', max_length=15)),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ResponseCustomer', to=settings.AUTH_USER_MODEL)),
                ('Jobrequest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Jobrequest', to='advertisement.jobrequest')),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='Location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='jobLocation', to='advertisement.savedaddress'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='Job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Upcoming_jobs', to='advertisement.job'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='Jobresponse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Jobresponse', to='advertisement.jobresponse'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='Technician',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Technician', to=settings.AUTH_USER_MODEL),
        ),
    ]