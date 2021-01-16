from django.db import models

# Create your models here.
class Item(models.Model):
    item=models.TextField(max_length=500, blank=True)
    description=models.TextField (max_length=900, blank=True)
    completed=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    type=models.TextField (max_length=100)
    image = models.ImageField(upload_to='images/', max_length=1000)

    def __str__(self):
        return self.item
