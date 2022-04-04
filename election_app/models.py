from django.db import models

class EVS_Admin(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Candidate(models.Model):
    # Candidate info
    candidate = models.CharField(max_length=255)
    votes = models.IntegerField()

class Voter(models.Model):
    no_dpt = models.IntegerField()
    vote = models.IntegerField(default=0)
