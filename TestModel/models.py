from django.db import models

# Create your models here.
class Test(models.Model):
    # name为字段，test为表名，前缀为包名即TestModel
    name = models.CharField(max_length=20)