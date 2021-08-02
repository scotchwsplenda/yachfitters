from django.shortcuts import redirect, render
from django.http import HttpResponse, QueryDict, HttpRequest, request, response
import pandas as pd
from .models import nfl_teams
from .forms import prediction_form
from datetime import datetime


def choose_team_view(request):
    team_view_form = nfl_teams.objects.all()
    team_acr = str(request.POST.get('butts'))
    if request.method=='POST':
        return redirect('cool_form_team', acr = team_acr)
        # return redirect(url name, parameter)
        # return cool_form_view(request, team_acr) this is also works but the URL will only be "/cool_form"
    return render(request, "brokerage/team.html", {'form': team_view_form})

# dif between return and redirect and sessions?

def cool_form_view(request, acr):
    url = 'https://www.pro-football-reference.com/teams/'+acr+'/2021.htm'
    table = pd.read_html(url, match='Game Results Table')
    df = table[0]
    df['Unnamed: 4'].fillna('VS.', inplace=True)
    df['Title'] = 'WEEK ' + df['Week']+' '+df['Unnamed: 4']+' '+df['Opp']
    schedule = df.loc[4:,'Title'].reset_index(drop=True)
    team_picked = nfl_teams.objects.get(team_acronym=acr)
    if request.method == "POST": #this refers to when the 'submit' button is clicked and the state changes
        form = prediction_form(request.POST)
        print(form)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.team = team_picked #for some dumb reason the form requires the full name but the table saves the acronym
            instance.Submitted_Date = datetime.now()
            # print(instance)
            instance.save()
            return redirect('/choose_team')
    else:
        form = prediction_form() # this is the blank form, before 'submit' has been hit
    return render(request, "brokerage/cool_form.html", {'season' : schedule , 'form':form, 'team':team_picked}) 

# initial = {'team ' : 'sea' ,'author' : 'OBL' ,'Hawk_Wk1' : 0 ,'Opp_Wk1' : 0 ,'Hawk_Wk2' : 0 ,'Opp_Wk2' : 0 ,'Hawk_Wk3' : 0 ,'Opp_Wk3' : 0 ,'Hawk_Wk4' : 0 ,'Opp_Wk4' : 0 ,'Hawk_Wk5' : 0 ,'Opp_Wk5' : 0 ,'Hawk_Wk6' : 0 ,'Opp_Wk6' : 0 ,'Hawk_Wk7' : 0 ,'Opp_Wk7' : 0 ,'Hawk_Wk8' : 0 ,'Opp_Wk8' : 0 ,'Hawk_Wk9' : 0 ,'Opp_Wk9' : 0 ,'Hawk_Wk10' : 0 ,'Opp_Wk10' : 0 ,'Hawk_Wk11' : 0 ,'Opp_Wk11' : 0 ,'Hawk_Wk12' : 0 ,'Opp_Wk12' : 0 ,'Hawk_Wk13' : 0 ,'Opp_Wk13' : 0 ,'Hawk_Wk14' : 0 ,'Opp_Wk14' : 0 ,'Hawk_Wk15' : 0 ,'Opp_Wk15' : 0 ,'Hawk_Wk16' : 0 ,'Opp_Wk16' : 0 ,'Hawk_Wk17' : 0 ,'Opp_Wk17' : 0 ,'Hawk_Wk18' : 0 ,'Opp_Wk18' : 0 ,'Submitted_Date': datetime.now()}

# , initial = {'team' : team_picked ,'author' : 'OBL'  ,'Submitted_Date': datetime.now()}