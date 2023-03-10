from django.db import models

class Netlify(models.Model):
    genetic = models.FloatField(null=True)
    length = models.FloatField(null=True)
    mass = models.FloatField(null=True)
    exercise = models.FloatField(null=True)
    smoking = models.FloatField(null=True)
    alcohol = models.FloatField(null=True)
    sugar = models.FloatField(null=True)
    lifespan = models.FloatField(null=True)

    def __str__(self):
        return f"""{self.genetic} {self.length} 
            {self.mass} {self.exercise} {self.smoking} 
            {self.alcohol} {self.sugar} {self.lifespan}"""