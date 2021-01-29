from django.db import models

class Movies(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=200)
    price = models.FloatField(null=True)

    def __str__(self):
        return self.name