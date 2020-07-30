# Generated by Django 3.0.1 on 2019-12-30 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bugtracker',
            name='Bug_type',
            field=models.CharField(choices=[('DB', 'Database'), ('FE', 'Frontend'), ('BE', 'Backend')], default='FE', max_length=2),
        ),
    ]
