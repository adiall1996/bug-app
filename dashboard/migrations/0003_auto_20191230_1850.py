# Generated by Django 3.0.1 on 2019-12-30 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_bugtracker_bug_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='dev_type',
            field=models.CharField(choices=[('DEV', 'Developer'), ('MAN', 'Manager'), ('SEN', 'Senior')], default='DEV', max_length=25),
        ),
        migrations.AlterField(
            model_name='bugtracker',
            name='Bug_status',
            field=models.CharField(choices=[('N', 'New'), ('F', 'Fixed'), ('R', 'Under Review')], default='New', max_length=25),
        ),
        migrations.AlterField(
            model_name='bugtracker',
            name='Bug_type',
            field=models.CharField(choices=[('DB', 'Database'), ('FE', 'Frontend'), ('BE', 'Backend')], default='FE', max_length=25),
        ),
    ]
