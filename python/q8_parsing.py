#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import csv
import pandas as pd

  def read_data(data):
    return pd.read_csv('data', index_col = 0)
    
  def get_team_min(parsed_data):
    diff = abs(parsed_data['Goals'] - parsed_data['Goals Allowed'])
    min_score = diff.min()
    team = [i for i in diff.index if diff[i] == min_score]
    for a in team:
      print(a, ' has the smallest difference', min_score,'in ‘for’ and ‘against’ goals.')
    
  

  def get_min_score_difference(self, parsed_data):
    # COMPLETE THIS FUNCTION

  def get_team(self, index_value, parsed_data):
    # COMPLETE THIS FUNCTION
