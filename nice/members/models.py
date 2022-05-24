from email.mime import image
from django.db import models

class Member(models.Model):
    nom=models.CharField(max_length=255)
    prenom=models.CharField(max_length=255)
    image=models.ImageField()
    description=models.CharField(max_length=255)
    def __str__(self):
        return self.nom +' ' +self.prenom

class Cell(models.Model):
    nom=models.CharField(max_length=255)
    description=models.TextField()
    image=models.ImageField()
    def __str__(self):
        return self.nom 


class Role(models.Model):
    role = models.CharField(
            choices=(('chef','chef'),('co-chef','co-chef'),('member','member')),
            blank=False,
            max_length=50
    )
    member=models.ForeignKey(Member, related_name='member',on_delete=models.CASCADE)    
    cell=models.ForeignKey(Cell, related_name='cell',on_delete=models.CASCADE)
    def __str__(self):
        return self.role
    
# Create your models here.
