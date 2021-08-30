from django.shortcuts import redirect, render
from django.http import HttpResponse, QueryDict, HttpRequest, request, response
import pandas as pd
from .models import nfl_teams, predicted_score
from .forms import prediction_form
from datetime import datetime
import numpy as np

def choose_team_view(request):
    team_view_form = nfl_teams.objects.all()
    team_acr = str(request.POST.get('butts'))
    if request.method=='POST':
        return redirect('cool_form_team', acr = team_acr)
    return render(request, "brokerage/team.html", {'form': team_view_form, 'phrase' : 'prognosticate on'})

def cool_form_view(request, acr):
    url = 'https://www.pro-football-reference.com/teams/'+acr+'/2021.htm'
    table = pd.read_html(url, match='Game Results Table')
    df = table[0]
    df['Unnamed: 4'].fillna('VS.', inplace=True)
    df['Title'] = +df['Unnamed: 4']+' '+df['Opp']+' -'+df['Day']+' '+df['Date']+' @ '+df['Unnamed: 3']
    cols = []
    for x in range(len(df)):
        y = df['Title'][x]
        cols.append(str(y))
    indy = [cols.index(x) for x in cols if x[-6:]=='Season']
    cols = cols[indy[0]+1:]
    weeks = ['W'+str(x+1)+' ' for x in range(18)]
    schedule = [i + j for i, j in zip(weeks, cols)]


    team_picked = nfl_teams.objects.get(team_acronym=acr)
    if request.method == "POST":
        form = prediction_form(request.POST)
        # form.fields['email'].required = False # this doesn't work and is obviated by making blank=True in the model
        if form.is_valid():
            instance = form.save(commit=False)
            instance.team = team_picked #the form requires the full name but the table saves the acronym
            instance.Submitted_Date = datetime.now() 
            instance.save() 
            return redirect('/results/{}'.format(acr))
    else:
        form = prediction_form() # this is the blank form, before 'submit' has been hit
    return render(request, "brokerage/cool_form.html", { 'season' : schedule , 'form':form, 'team':team_picked}) 

def highlight_max(cell): 
    if type(cell) == str:
        return 'background: white; color: black' #; border: 1px solid black
    if type(cell) != str and cell < 0 : 
        return 'background: white; color:red'
    else: 
        return 'background: white; color: green'

def choose_results_view(request):
    team_view_form = nfl_teams.objects.all()
    team_acr = str(request.POST.get('butts'))
    if request.method=='POST':
        return redirect('results_team', acr = team_acr)
        # return cool_form_view(request, team_acr) this is also works but the URL will only be "/cool_form"
    return render(request, "brokerage/team.html", {'form': team_view_form, 'phrase' : 'see what people are prognosticating'})

# https://stackoverflow.com/questions/13148429/how-to-change-the-order-of-dataframe-columns
def results_view(request, acr):
    result = pd.DataFrame(list(predicted_score.objects.all().filter(team = acr).values()))
    result = result.set_index('author')
    hawkscore_df = result.iloc[:,3:-1:2]
    oppscore_df = result.iloc[:,4:-1:2]

    url = 'https://www.pro-football-reference.com/teams/'+acr+'/2021.htm'
    table = pd.read_html(url, match='Game Results Table')
    df = table[0]
    cols = []
    for x in range(len(df)):
        y = df['Opp'][x]
        cols.append(str(y).split()[-1])
    indy = cols.index('Season')
    cols = cols[indy+1:]
    new_col = ['Pigskins' if word == 'Team' else 'Bye' if word == 'Week' else word for word in cols]
    weeks = ['W'+str(x+1)+' ' for x in range(18)]
    res = [i + j for i, j in zip(weeks, new_col)]
    hawkscore_df.columns = res
    oppscore_df.columns = res

    proggs = hawkscore_df.astype(str).add(' - ').add(oppscore_df.astype(str))
    proggs.reset_index(level=0, inplace=True)
    proggs = proggs.to_html(classes="table table-striped table-bordered table-hover", border=1,  index=False)

    spreads = hawkscore_df.subtract(oppscore_df)
    spreads.reset_index(level=0, inplace=True)

    predicted_record = {'author' : spreads['author'] , "Wins" : (spreads.iloc[:, 1:] > 0).sum(axis=1),
    "Losses" : (spreads.iloc[:, 1:] < 0).sum(axis=1), "Ties" : (spreads.iloc[:, 1:] == 0).sum(axis=1),
    "Differential" : (spreads.iloc[:, 1:]).sum(axis=1)}
    result = pd.DataFrame(predicted_record)

    average_record = pd.DataFrame(columns=['Dude', 'Wins', 'Losses', 'Differential'])
    average_record.loc[1] = ['Mean', round(result['Wins'].mean()),round(abs(17 - result['Wins'].mean())), round(result['Differential'].mean())]
    average_record.loc[2] = ['Mode', result['Wins'].mode()[0],result['Losses'].mode()[0], result['Differential'].mode()[0]]
    average_record.loc[3] = ['Median', round(result['Wins'].median()),round(abs(17 - result['Wins'].median())), round(result['Differential'].median())]
    ints = ['Wins', 'Losses', 'Differential']
    average_record[ints] = average_record[ints].astype(int)
    average_record["Differential"]=average_record["Differential"].astype(str).apply(lambda x: f"+{x}" if int(x)>0 else x)
    average_record = average_record.to_html(classes="table table-striped table-bordered table-hover", border=1,  index=False)

    result["Differential"]=result["Differential"].astype(str).apply(lambda x: f"+{x}" if int(x)>0 else x)
    result = result.sort_values(["Wins", "Differential"], ascending = (False, False))
    result = result.to_html(classes="table table-striped table-bordered table-hover", border=1,  index=False)

    spreads = spreads.style.applymap(highlight_max).hide_index().set_table_attributes('border="1" class="dataframe table table-hover table-bordered table-striped"').render()

    overunders = hawkscore_df.add(oppscore_df)
    overunders.reset_index(level=0, inplace=True)
    overunders = overunders.to_html(classes="table table-striped table-bordered table-hover", border=1,  index=False)

    
    
    return render(request, "brokerage/results_team.html", {'spreads' : spreads, 'overunders':overunders, 'proggs':proggs, 'result':result, 'average_record':average_record})
    
    # {'spreads_html' : spreads_html, 'record' : result.to_html(classes="table table-striped table-bordered table-hover", index=False, border=1),'average_record':average_record.to_html(classes="table table-striped table-bordered table-hover", index=False, border=1) })

