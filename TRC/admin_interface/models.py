from django.db import models

class PageText(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name