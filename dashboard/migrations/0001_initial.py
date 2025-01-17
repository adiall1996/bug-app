# Generated by Django 3.0.1 on 2019-12-30 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='BugTracker',
            fields=[
                ('Bug_id', models.AutoField(primary_key=True, serialize=False)),
                ('Bug_Title', models.CharField(max_length=255)),
                ('Comments', models.CharField(max_length=255)),
                ('Bug_status', models.CharField(choices=[('N', 'New'), ('F', 'Fixed'), ('R', 'Under Review')], default='New', max_length=2)),
                ('Bug_image', models.ImageField(upload_to='uploads/')),
                ('Bug_Deadline', models.DateTimeField(auto_now_add=True)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.Developer')),
            ],
        ),
        migrations.CreateModel(
            name='Assign_developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bug_Id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.BugTracker')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.Developer')),
            ],
        ),
    ]
