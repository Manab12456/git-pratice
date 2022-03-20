from django.db import models
from datetime import datetime

class Tasks(models.Model):
    types_choice=(
        ('Personal','Personal'),
        ('Shopping','Shopping'),
        ('Wishlist','Wishlist'),
        ('Office','Office'),
        ('Custom','Custom'),
    )
    type= models.CharField(max_length=35,choices=types_choice)
    title= models.CharField(max_length=35)
    description= models.TextField()
    due_date= models.DateTimeField(null=True)
    remainder= models.DateTimeField(null=True)
    created_at= models.DateTimeField(default=datetime.now())
    finised= models.BooleanField(default=False,blank=True)

    class Meta:
        ordering = ('created_at',)