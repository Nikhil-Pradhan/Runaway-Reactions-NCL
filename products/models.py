from django.db import models

class Reactions(models.Model):
    reaction_id = models.IntegerField(null=True)
    reaction_desc = models.CharField(max_length=1024, null=True)
    reactants = models.CharField(max_length=1024, null=True)
    products = models.CharField(max_length=1024, null=True)
    yield_percent = models.CharField(max_length=20, null=True)
    additional_products = models.CharField(max_length=1024, null=True)
    steps = models.IntegerField(null=True)
    stages = models.CharField(max_length=1024, null=True)
    reagents = models.CharField(max_length=1024, null=True)
    catalyst = models.CharField(max_length=1024, null=True)
    solvents = models.CharField(max_length=1024, null=True)
    conditions = models.CharField(max_length=1024, null=True)
    time = models.CharField(max_length=1024, null=True)
    temp = models.CharField(max_length=1024, null=True)
    pressure = models.CharField(max_length=20, null=True)
    Lit_ref = models.CharField(max_length=2048, null=True)
    endo_exo = models.CharField(max_length=20, null=True)
    cas_member_method = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name_plural = "Reactions"