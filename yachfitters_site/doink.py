# a way to make a df by first creating a dictionary of lists:
predicted_record = {'Dude' : predicted['Dude'] , "Wins" : (predicted.iloc[:, 1:] > 0).sum(axis=1),
"Losses" : (predicted.iloc[:, 1:] < 0).sum(axis=1), "Ties" : (predicted.iloc[:, 1:] == 0).sum(axis=1),
"Differential" : (predicted.iloc[:, 1:]).sum(axis=1)}

result = pd.DataFrame(predicted_record)

average_record = pd.DataFrame(columns=['Dude', 'Wins', 'Losses', 'Differential'])
average_record.loc[1] = ['Mean', round(result['Wins'].mean()),round(abs(17 - result['Wins'].mean())), round(result['Differential'].mean())]
average_record.loc[2] = ['Mode', result['Wins'].mode()[0],result['Losses'].mode()[0], result['Differential'].mode()[0]]
average_record.loc[3] = ['Median', round(result['Wins'].median()),round(abs(17 - result['Wins'].median())), round(result['Differential'].median())]
ints = ['Wins', 'Losses', 'Differential']
average_record[ints] = average_record[ints].astype(int)
average_record["Differential"]=average_record["Differential"].astype(str).apply(lambda x: f"+{x}" if int(x)>0 else x)

result["Differential"]=result["Differential"].astype(str).apply(lambda x: f"+{x}" if int(x)>0 else x)
result = result.sort_values(["Wins", "Differential"], ascending = (False, False))

spreads = predicted.sort_values(["Dude"]) #.to_html(classes="table table-striped table-bordered table-hover", index=False)
spreads_html = spreads.style.applymap(highlight_max).hide_index().set_table_attributes('border="1" class="dataframe table table-hover table-bordered table-striped"').render()

# initial = {'team ' : 'sea' ,'author' : 'OBL' ,'Hawk_Wk1' : 0 ,'Opp_Wk1' : 0 ,'Hawk_Wk2' : 0 ,'Opp_Wk2' : 0 ,'Hawk_Wk3' : 0 ,'Opp_Wk3' : 0 ,'Hawk_Wk4' : 0 ,'Opp_Wk4' : 0 ,'Hawk_Wk5' : 0 ,'Opp_Wk5' : 0 ,'Hawk_Wk6' : 0 ,'Opp_Wk6' : 0 ,'Hawk_Wk7' : 0 ,'Opp_Wk7' : 0 ,'Hawk_Wk8' : 0 ,'Opp_Wk8' : 0 ,'Hawk_Wk9' : 0 ,'Opp_Wk9' : 0 ,'Hawk_Wk10' : 0 ,'Opp_Wk10' : 0 ,'Hawk_Wk11' : 0 ,'Opp_Wk11' : 0 ,'Hawk_Wk12' : 0 ,'Opp_Wk12' : 0 ,'Hawk_Wk13' : 0 ,'Opp_Wk13' : 0 ,'Hawk_Wk14' : 0 ,'Opp_Wk14' : 0 ,'Hawk_Wk15' : 0 ,'Opp_Wk15' : 0 ,'Hawk_Wk16' : 0 ,'Opp_Wk16' : 0 ,'Hawk_Wk17' : 0 ,'Opp_Wk17' : 0 ,'Hawk_Wk18' : 0 ,'Opp_Wk18' : 0 ,'Submitted_Date': datetime.now()}
