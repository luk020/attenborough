from django.db import models
from django.forms import ModelForm

# Create your models here.

class Show(models.Model):
    name = models.CharField(max_length=64)
    year = models.PositiveSmallIntegerField()
    eps = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.name} ({self.year})"
    
class Event(models.Model):
    show_id = models.ForeignKey(Show, on_delete=models.CASCADE, related_name="events")
    episode = models.PositiveSmallIntegerField()
    animal = models.CharField(max_length=32)
    continent = models.CharField(max_length=32)
    location = models.CharField(max_length=32)
    time = models.CharField(max_length=32)
    description = models.CharField(max_length=256)

    def  __str__(self):
        return f"Episode {self.episode} || {self.animal} in {self.continent} - {self.description}."
    
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
