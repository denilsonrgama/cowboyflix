from django.db import models

#Classe genero
class Genre(models.Model):
    name = models.CharField(max_length=200)    
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name    