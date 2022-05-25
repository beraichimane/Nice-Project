from django.db import models
class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="thumbnail")
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class EventLink(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class EventLocalisation(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE,primary_key=True)
    locale_name = models.CharField(max_length=255)
    x_locale = models.DecimalField(max_digits=9, decimal_places=6)
    y_locale = models.DecimalField(max_digits=9, decimal_places=6)
    def __str__(self):
        return self.locale_name

class Sponsors(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()