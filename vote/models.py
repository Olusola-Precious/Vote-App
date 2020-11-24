from django.db import models

# Create your models here.

class Contestants(models.Model):
    name = models.CharField(max_length=100)
    
    def calculateVotes(self):
        c_id = Contestants.objects.get(name=self)
        return Voters.objects.filter(vote=c_id.id).count()
    
    votes = property(calculateVotes)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "Contestants_Info"
        verbose_name = "Contestant"
        verbose_name_plural = "Contestants"

    

class Voters(models.Model):
    email = models.CharField(max_length=300, unique=True,blank=False, null=False)
    vote = models.CharField(max_length=30, null=True, blank=True)
    voted = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.email
    
    class Meta:
        ordering = ('email')

    
    class Meta:
        db_table = "Voters_Info"
        verbose_name = "Voter"
        verbose_name_plural = "Voters"

    
