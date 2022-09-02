from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=50)
    group = models.CharField(max_length=100)
    capacity = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to='user/',null=True,blank=True)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
