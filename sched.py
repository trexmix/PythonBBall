import csv
import datetime, time

CONST_DATE = 0
CONST_VISITOR = 2
CONST_HOME = 4

date = datetime.datetime.now()
CONST_TODAYS_DATE = date = datetime.date(date.year, date.month, date.day)



def main():
    with open('nba_sched_csv.csv', 'rt') as c:
        reader = csv.reader(c)
        threeGamesFourDays(reader)

    with open('nba_sched_csv.csv', 'rt') as c:
        reader = csv.reader(c)
        backToBack(reader)

def backToBack(reader):
    teams = {
        'Atlanta Hawks': 0,
        'Boston Celtics': 0,
        'Brooklyn Nets': 0,
        'Charlotte Hornets': 0,
        'Chicago Bulls': 0,
        'Cleveland Cavaliers': 0,
        'Dallas Mavericks': 0,
        'Denver Nuggets': 0,
        'Detroit Pistons': 0,
        'Golden State Warriors': 0,
        'Houston Rockets': 0,
        'Indiana Pacers': 0,
        'Los Angeles Clippers': 0,
        'Los Angeles Lakers': 0,
        'Memphis Grizzlies': 0,
        'Miami Heat': 0,
        'Milwaukee Bucks': 0,
        'Minnesota Timberwolves': 0,
        'New Orleans Pelicans': 0,
        'New York Knicks': 0,
        'Oklahoma City Thunder': 0,
        'Orlando Magic': 0,
        'Philadelphia 76ers': 0,
        'Phoenix Suns': 0,
        'Portland Trail Blazers': 0,
        'Sacramento Kings': 0,
        'San Antonio Spurs': 0,
        'Toronto Raptors': 0,
        'Utah Jazz': 0,
        'Washington Wizards': 0
    }
    
    for key, value in teams.items():
        value = 0
    
    for game in reader:
        gameDate = gamePythonDate(game)                                              
        if gameWithinNDays(game, 1):
            teams[game[CONST_VISITOR]] += 1
            teams[game[CONST_HOME]] += 1

    print("Teams with a back to back")
    print("-------------------------")

    print(teams)
    
    for key, value in teams.items():
        if value >= 2:
            print(key)       

def threeGamesFourDays(reader):
    teams = {
        'Atlanta Hawks': 0,
        'Boston Celtics': 0,
        'Brooklyn Nets': 0,
        'Charlotte Hornets': 0,
        'Chicago Bulls': 0,
        'Cleveland Cavaliers': 0,
        'Dallas Mavericks': 0,
        'Denver Nuggets': 0,
        'Detroit Pistons': 0,
        'Golden State Warriors': 0,
        'Houston Rockets': 0,
        'Indiana Pacers': 0,
        'Los Angeles Clippers': 0,
        'Los Angeles Lakers': 0,
        'Memphis Grizzlies': 0,
        'Miami Heat': 0,
        'Milwaukee Bucks': 0,
        'Minnesota Timberwolves': 0,
        'New Orleans Pelicans': 0,
        'New York Knicks': 0,
        'Oklahoma City Thunder': 0,
        'Orlando Magic': 0,
        'Philadelphia 76ers': 0,
        'Phoenix Suns': 0,
        'Portland Trail Blazers': 0,
        'Sacramento Kings': 0,
        'San Antonio Spurs': 0,
        'Toronto Raptors': 0,
        'Utah Jazz': 0,
        'Washington Wizards': 0
    }

    
    for game in reader:
        gameDate = gamePythonDate(game)                                              
        if gameWithinNDays(game, 3):
            teams[game[CONST_VISITOR]] += 1
            teams[game[CONST_HOME]] += 1

    print("Teams with 3 in 4")
    print("-------------------------")
    for key, value in teams.items():
        if value >= 3:
            print(key)
        
def doesGameInvolve(team, game):
    return game[CONST_VISITOR] == team or game[CONST_HOME] == team

def gamePythonDate(game):
    splitDate = game[CONST_DATE].split(" ")
            
    return datetime.date(int(splitDate[3]), monthToNum(splitDate[1]), int(splitDate[2])) 

def gameWithinNDays(game, n):
    margin = datetime.timedelta(days = n)

    return CONST_TODAYS_DATE <= gamePythonDate(game) <= CONST_TODAYS_DATE + margin

def monthToNum(shortMonth):

    return{
            'Jan' : 1,
            'Feb' : 2,
            'Mar' : 3,
            'Apr' : 4,
            'May' : 5,
            'Jun' : 6,
            'Jul' : 7,
            'Aug' : 8,
            'Sep' : 9, 
            'Oct' : 10,
            'Nov' : 11,
            'Dec' : 12
    }[shortMonth]

main()
        
