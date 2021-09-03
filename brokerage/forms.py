
from .models import predicted_score, nfl_teams
from django.forms import ModelForm

class prediction_form(ModelForm):
    class Meta:
        model = predicted_score
        fields = '__all__'
        exclude = ('team', 'submitted_date')

# class prediction_form(forms.Form):
#     team = forms.CharField(max_length=3)
#     author= forms.CharField(max_length=420)
#     Hawk_Wk1= forms.IntegerField(default=0)
#     Opp_Wk1= forms.IntegerField(default=0)
#     Hawk_Wk2= forms.IntegerField(default=0)
#     Opp_Wk2= forms.IntegerField(default=0)
#     Hawk_Wk3= forms.IntegerField(default=0)
#     Opp_Wk3= forms.IntegerField(default=0)
#     Hawk_Wk4= forms.IntegerField(default=0)
#     Opp_Wk4= forms.IntegerField(default=0)
#     Hawk_Wk5= forms.IntegerField(default=0)
#     Opp_Wk5= forms.IntegerField(default=0)
#     Hawk_Wk6= forms.IntegerField(default=0)
#     Opp_Wk6= forms.IntegerField(default=0)
#     Hawk_Wk7= forms.IntegerField(default=0)
#     Opp_Wk7= forms.IntegerField(default=0)
#     Hawk_Wk8= forms.IntegerField(default=0)
#     Opp_Wk8=forms.IntegerField(default=0)
#     Hawk_Wk9= forms.IntegerField(default=0)
#     Opp_Wk9= forms.IntegerField(default=0)
#     Hawk_Wk10= forms.IntegerField(default=0)
#     Opp_Wk10= forms.IntegerField(default=0)
#     Hawk_Wk11= forms.IntegerField(default=0)
#     Opp_Wk11= forms.IntegerField(default=0)
#     Hawk_Wk12= forms.IntegerField(default=0)
#     Opp_Wk12= forms.IntegerField(default=0)
#     Hawk_Wk13= forms.IntegerField(default=0)
#     Opp_Wk13= forms.IntegerField(default=0)
#     Hawk_Wk14= forms.IntegerField(default=0)
#     Opp_Wk14= forms.IntegerField(default=0)
#     Hawk_Wk15= forms.IntegerField(default=0)
#     Opp_Wk15= forms.IntegerField(default=0)
#     Hawk_Wk16= forms.IntegerField(default=0)
#     Opp_Wk16= forms.IntegerField(default=0)
#     Hawk_Wk17= forms.IntegerField(default=0)
#     Opp_Wk17= forms.IntegerField(default=0)
#     Hawk_Wk18= forms.IntegerField(default=0)
#     Opp_Wk18= forms.IntegerField(default=0)
#     Submitted_Date = forms.DateField( null=True)