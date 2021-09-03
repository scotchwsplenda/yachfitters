from django.db import models
from django.contrib.auth import get_user_model

from django.conf import settings

# from django.db.models.fields import related


# https://docs.djangoproject.com/en/3.1/howto/legacy-databases/ -> python manage.py inspectdb
# https://datatofish.com/pandas-dataframe-to-sql/
# Create your models here.
# install SQLITE Explorer extension

class nfl_teams(models.Model):
    team_name = models.CharField(max_length=420)
    team_acronym = models.CharField(max_length=3, primary_key=True)
    def __str__(self):
        return self.team_name

class predicted_score(models.Model):
    id = models.AutoField(primary_key=True)
    team = models.ForeignKey(nfl_teams, on_delete=models.CASCADE)
    author= models.CharField(max_length=420, null=True, unique=True)
    email = models.EmailField(null=True, blank=True)
    Hawk_Wk1= models.PositiveIntegerField(default=0, null=True)
    Opp_Wk1= models.PositiveIntegerField(default=0, null=True)
    Hawk_Wk2= models.PositiveIntegerField(default=0, null=True)
    Opp_Wk2= models.PositiveIntegerField(default=0, null=True)
    Hawk_Wk3= models.PositiveIntegerField(default=0, null=True)
    Opp_Wk3= models.PositiveIntegerField(default=0, null=True)
    Hawk_Wk4= models.PositiveIntegerField(default=0, null=True)
    Opp_Wk4= models.PositiveIntegerField(default=0, null=True)
    Hawk_Wk5= models.PositiveIntegerField(default=0, null=True)
    Opp_Wk5= models.PositiveIntegerField(default=0, null=True)
    Hawk_Wk6= models.PositiveIntegerField(default=0, null=True)
    Opp_Wk6= models.PositiveIntegerField(default=0, null=True)
    Hawk_Wk7= models.PositiveIntegerField(default=0, null=True)
    Opp_Wk7= models.PositiveIntegerField(default=0, null=True)
    Hawk_Wk8= models.PositiveIntegerField(default=0, null=True)
    Opp_Wk8=models.PositiveIntegerField(default=0, null=True)
    Hawk_Wk9= models.PositiveIntegerField(default=0, null=True)
    Opp_Wk9= models.PositiveIntegerField(default=0, null=True)
    Hawk_Wk10= models.PositiveIntegerField(default=0, null=True)
    Opp_Wk10= models.PositiveIntegerField(default=0, null=True)
    Hawk_Wk11= models.PositiveIntegerField(default=0, null=True)
    Opp_Wk11= models.PositiveIntegerField(default=0, null=True)
    Hawk_Wk12= models.PositiveIntegerField(default=0, null=True)
    Opp_Wk12= models.PositiveIntegerField(default=0, null=True)
    Hawk_Wk13= models.PositiveIntegerField(default=0, null=True)
    Opp_Wk13= models.PositiveIntegerField(default=0, null=True)
    Hawk_Wk14= models.PositiveIntegerField(default=0, null=True)
    Opp_Wk14= models.PositiveIntegerField(default=0, null=True)
    Hawk_Wk15= models.PositiveIntegerField(default=0, null=True)
    Opp_Wk15= models.PositiveIntegerField(default=0, null=True)
    Hawk_Wk16= models.PositiveIntegerField(default=0, null=True)
    Opp_Wk16= models.PositiveIntegerField(default=0, null=True)
    Hawk_Wk17= models.PositiveIntegerField(default=0, null=True)
    Opp_Wk17= models.PositiveIntegerField(default=0, null=True)
    Hawk_Wk18= models.PositiveIntegerField(default=0, null=True)
    Opp_Wk18= models.PositiveIntegerField(default=0, null=True)
    Submitted_Date = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.author