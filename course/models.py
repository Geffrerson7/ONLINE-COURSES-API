from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    
    product_code = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    image = models.URLField(max_length=500)
    description = models.TextField(max_length=500)
    price = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, name="user")

    def __str__(self):
        return self.product_code

    class Meta:
        db_table = "Course"
