# Generated by Django 3.2.10 on 2022-01-11 21:04

import datetime
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import sars_dashboard.reports.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('zip_file', models.FileField(storage=django.core.files.storage.FileSystemStorage(base_url='/protected', location='/app/sars_dashboard/protected'), upload_to='report-zipped')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('belongs_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='projects.project', verbose_name='Project')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='ReportIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(max_length=255, storage=django.core.files.storage.FileSystemStorage(base_url='/protected', location='/app/sars_dashboard/protected'), upload_to=sars_dashboard.reports.models.get_report_path)),
                ('original_name', models.CharField(blank=True, max_length=255)),
                ('zipped_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='index', to='reports.report', verbose_name='Index')),
            ],
        ),
        migrations.CreateModel(
            name='ReportFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(max_length=255, storage=django.core.files.storage.FileSystemStorage(base_url='/protected', location='/app/sars_dashboard/protected'), upload_to=sars_dashboard.reports.models.get_report_path)),
                ('original_name', models.CharField(blank=True, max_length=255)),
                ('is_index', models.BooleanField(default=False)),
                ('zipped_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='reports.report', verbose_name='Files')),
            ],
        ),
    ]
