from django.db import models
from django.core.validators import MaxValueValidator


class Movies(models.Model):
    title = models.CharField(max_length=50)
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
    	verbose_name_plural="Movies"
