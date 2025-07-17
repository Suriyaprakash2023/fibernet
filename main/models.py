
from django.db import models

class Enquiry(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    mobile = models.CharField(max_length=15,null=True,blank=True)
    message = models.TextField(blank=True,null=True)
    is_enquiryed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.name
