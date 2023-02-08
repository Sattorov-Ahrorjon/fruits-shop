from django.db import models


class Fruit(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    about = models.TextField(max_length=600)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-time"]
