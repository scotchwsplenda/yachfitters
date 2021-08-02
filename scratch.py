import pandas as pd

url = 'https://www.pro-football-reference.com/teams/sea/2021.htm'
table = pd.read_html(url, match='Game Results Table')
df = table[0]
df['Unnamed: 4'].fillna('VS.', inplace=True)
df['SCHEDULE'] = 'WEEK ' + df['Week']+' '+df['Unnamed: 4']+' '+df['Opp']
df.reset_index(inplace=True)
print(df.loc[5:,'SCHEDULE'])
