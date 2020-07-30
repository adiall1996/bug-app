from django.db import models




# Create your models here.

STATUS = [
    ('N', 'New'),
    ('F', 'Fixed'),
    ('R', 'Under Review'),
]

TYPE = [
    ('DB', 'Database'),
    ('FE', 'Frontend'),
    ('BE', 'Backend'),
]

POSITION = [
    ('DEV', 'Developer'),
    ('MAN', 'Manager'),
    ('SEN', 'Senior'),

]

class Developer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=250)
    dev_type = models.CharField(
        max_length=25,
        choices=POSITION,
        default='DEV',
    )

def __str__(self):
    return self.Developer.name
class BugTracker(models.Model):
    Bug_id = models.AutoField(primary_key=True)
    Bug_Title = models.CharField(max_length=255)
    Comments = models.CharField(max_length=255)
    Bug_status = models.CharField(
        max_length=25,
        choices=STATUS,
        default='New',
    )
    Bug_type = models.CharField(
        max_length=25,
        choices=TYPE,
        default='FE',
    )
    Bug_image = models.ImageField(upload_to='uploads/', height_field=None, width_field=None, max_length=100,blank=True)
    Bug_Deadline = models.DateTimeField(auto_now_add=True)
    email = models.ForeignKey(Developer, on_delete=models.PROTECT)





class Assign_developer(models.Model):
    Bug_Id = models.ForeignKey(BugTracker,on_delete=models.PROTECT)
    email = models.ForeignKey(Developer, on_delete=models.PROTECT)
    deadline = models.DateTimeField

