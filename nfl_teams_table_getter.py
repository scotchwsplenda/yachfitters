from bs4 import BeautifulSoup
import requests

# https://stackoverflow.com/questions/42285417/how-to-preserve-links-when-scraping-a-table-with-beautiful-soup-and-pandas
r = requests.get('https://www.pro-football-reference.com/teams/')
soup=BeautifulSoup(r.text,'html.parser')
table = soup.find_all('table')[0] #reqires the [0] for some reason
links = []
for tr in table.findAll("tr"):
    trs = tr.findAll("th")
    for each in trs:
        try:
            # the find('a') refers to an HTML tag
            links.append([str(each.find('a')['href']).split('/')[2],str(each.find('a')).split('>')[1].replace('</a','')])
        except:
            pass

[print(str(item[0:])[1:-1]) for item in links]


# THE SQL
# INSERT INTO brokerage_nfl_teams (team_acronym, team_name) VALUES ('sea', 'Seattle Seahawks');
# INSERT INTO brokerage_nfl_teams (team_acronym, team_name) VALUES ('crd', 'Arizona Cardinals');
# INSERT INTO brokerage_nfl_teams (team_acronym, team_name) VALUES ('atl', 'Atlanta Falcons');
# INSERT INTO brokerage_nfl_teams (team_acronym, team_name) VALUES ('rav', 'Baltimore Ravens');
# INSERT INTO brokerage_nfl_teams (team_acronym, team_name) VALUES ('buf', 'Buffalo Bills');
# INSERT INTO brokerage_nfl_teams (team_acronym, team_name) VALUES ('car', 'Carolina Panthers');
# INSERT INTO brokerage_nfl_teams (team_acronym, team_name) VALUES ('chi', 'Chicago Bears');
# INSERT INTO brokerage_nfl_teams (team_acronym, team_name) VALUES ('cin', 'Cincinnati Bengals');
# INSERT INTO brokerage_nfl_teams (team_acronym, team_name) VALUES ('cle', 'Cleveland Browns');
# INSERT INTO brokerage_nfl_teams (team_acronym, team_name) VALUES ('dal', 'Dallas Cowboys');
# INSERT INTO brokerage_nfl_teams (team_acronym, team_name) VALUES ('den', 'Denver Broncos');
# INSERT INTO brokerage_nfl_teams (team_acronym, team_name) VALUES ('det', 'Detroit Lions');
# INSERT INTO brokerage_nfl_teams (team_acronym, team_name) VALUES ('gnb', 'Green Bay Packers');
# INSERT INTO brokerage_nfl_teams (team_acronym, team_name) VALUES ('htx', 'Houston Texans');
# INSERT INTO brokerage_nfl_teams (team_acronym, team_name) VALUES ('clt', 'Indianapolis Colts');
# INSERT INTO brokerage_nfl_teams (team_acronym, team_name) VALUES ('jax', 'Jacksonville Jaguars');
# INSERT INTO brokerage_nfl_teams (team_acronym, team_name) VALUES ('kan', 'Kansas City Chiefs');
# INSERT INTO brokerage_nfl_teams (team_acronym, team_name) VALUES ('rai', 'Las Vegas Raiders');
# INSERT INTO brokerage_nfl_teams (team_acronym, team_name) VALUES ('sdg', 'Los Angeles Chargers');
# INSERT INTO brokerage_nfl_teams (team_acronym, team_name) VALUES ('ram', 'Los Angeles Rams');
# INSERT INTO brokerage_nfl_teams (team_acronym, team_name) VALUES ('mia', 'Miami Dolphins');
# INSERT INTO brokerage_nfl_teams (team_acronym, team_name) VALUES ('min', 'Minnesota Vikings');
# INSERT INTO brokerage_nfl_teams (team_acronym, team_name) VALUES ('nwe', 'New England Patriots');
# INSERT INTO brokerage_nfl_teams (team_acronym, team_name) VALUES ('nor', 'New Orleans Saints');
# INSERT INTO brokerage_nfl_teams (team_acronym, team_name) VALUES ('nyg', 'New York Giants');
# INSERT INTO brokerage_nfl_teams (team_acronym, team_name) VALUES ('nyj', 'New York Jets');
# INSERT INTO brokerage_nfl_teams (team_acronym, team_name) VALUES ('phi', 'Philadelphia Eagles');
# INSERT INTO brokerage_nfl_teams (team_acronym, team_name) VALUES ('pit', 'Pittsburgh Steelers');
# INSERT INTO brokerage_nfl_teams (team_acronym, team_name) VALUES ('sfo', 'San Francisco 49ers');
# INSERT INTO brokerage_nfl_teams (team_acronym, team_name) VALUES ('tam', 'Tampa Bay Buccaneers');
# INSERT INTO brokerage_nfl_teams (team_acronym, team_name) VALUES ('oti', 'Tennessee Titans');
# INSERT INTO brokerage_nfl_teams (team_acronym, team_name) VALUES ('was', 'Washington Football Team');
# -- select * from brokerage_nfl_teams

# --delete  from  brokerage_nfl_teams