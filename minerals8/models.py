from django.db import models
import json


# Create your models here.
class Mineral(models.Model):
    """creates model instance"""
    """Makes instance of mineral with its associated attributes"""
    name = models.CharField(max_length=200)
    image_filename = models.CharField(max_length=300, null=True)
    image_caption = models.CharField(max_length=300, null=True)
    category = models.CharField(max_length=200, null=True)
    formula = models.CharField(max_length=400, null=True)
    strunz_classification = models.CharField(max_length=300, null=True)
    color = models.CharField(max_length=200, null=True)
    crystal_system = models.CharField(max_length=200, null=True)
    unit_cell = models.CharField(max_length=200, null=True)
    crystal_symmetry = models.CharField(max_length=200, null=True)
    cleavage = models.CharField(max_length=200, null=True)
    mohs_scale_hardness = models.CharField(max_length=200, null=True)
    luster = models.CharField(max_length=200, null=True)
    streak = models.CharField(max_length=200, null=True)
    diaphaneity = models.CharField(max_length=200, null=True)
    optical_properties = models.CharField(max_length=200, null=True)
    refractive_index = models.CharField(max_length=200, blank=True, default='')
    crystal_habit = models.CharField(max_length=200, blank=True, default='')
    specific_gravity = models.CharField(max_length=200, blank=True, default='')

    def __str__(self):
        return self.name
