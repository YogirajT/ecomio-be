import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

class DestinationModel(models.Model):
    id = models.AutoField(editable=False, primary_key=True)

    content = models.TextField()
    air_quality = models.SmallIntegerField(default= 0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    water_quality = models.SmallIntegerField(default= 0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    energy_sources = models.SmallIntegerField(default= 0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    createdAt = models.DateTimeField(auto_now_add=True, null=True)
    updatedAt = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = "destination"

        def __str__(self) -> str:
            return self.content


class SearchDataModel(models.Model):
    id = models.AutoField(editable=False, primary_key=True)

    url = models.CharField(max_length=4096)
    data = models.TextField()

    createdAt = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = "search_data"

        def __str__(self) -> str:
            return self.content