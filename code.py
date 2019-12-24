# --------------
import yaml
# Read the data of the format .yaml type
with open(path) as f:
    data = yaml.load(f)
# Find data type of the file
print(type(data))
#print(data)
x= print(data.keys())
data.get('info')
# In which city, and at which venue the match was played and where was it played ?
city = data.get('info').get('city')
print("The match was played at " +city )
venue = data.get('info').get('venue')
print("The match was played at ground " +venue )
# Which are all the teams that played in the tournament ? How many teams participated in total?
teams= str(data.get('info').get('teams'))
print("Teams played in tournament: "+teams)
# Which team won the toss and what was the decision of toss winner ?
print(data.get('info'))
winner = str(data.get('info').get('toss').get('winner'))
print("Toss won by "+ winner)
decision = str(data.get('info').get('toss').get('decision'))
print('Dicision of toss winner is '+ decision)
# Find the first bowler and first batsman who played the first ball of the first inning
#print(data.get('innings'))
batsman = str(data.get('innings')[0].get('1st innings').get('deliveries')[0].get(0.1).get('batsman'))
print('First batsman is '+ batsman)
bowler = str(data.get('innings')[0].get('1st innings').get('deliveries')[0].get(0.1).get('bowler'))
print('First bowler is '+ bowler)
# How many deliveries were delivered in first inning ?
number1 = len(data.get('innings')[0].get('1st innings').get('deliveries'))
print(number1)
# How many deliveries were delivered in second inning ?
number2 = len(data.get('innings')[1].get('2nd innings').get('deliveries'))
print(number2)
# Which team won and how ?
win = str(data.get('info').get('outcome').get('winner'))
runs= str(data.get('info').get('outcome').get('by').get('runs'))
print('Match won by '+win+ ' by '+runs+ ' runs')





