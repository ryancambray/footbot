from twython import Twython
import requests
import json
import tokens
from datetime import datetime

"""
example response

{"data": [
    {"federation": "UEFA", "home_team": "Manchester City", "prediction": "1", "status": "pending", "season": "2017 - 2018", "start_date": "2018-04-22T16:30:00", "result": "", 
    "odds": {"X": 8.458, "12": 1.053, "2": 20.46, "X2": 5.864, "1": 1.135, "1X": 1.013}, "id": 13249, "competition_cluster": "England", 
    "last_update_at": "2018-04-22T14:06:35.857000", "competition_name": "Premiership", "is_expired": false, "away_team": "Swansea"}]}

{'data': [{'odds': {'2': 6.37, 'X': 3.911, '1X': 1.113, '12': 1.213, '1': 1.553, 'X2': 2.466}, 'home_team': 'Atletico Madrid', 'prediction': '1', 'status': 'pending', 'id': 13287, 'start_date': '2018-04-22T19:45:00', 'competition_name': 'Primera Division', 'season': '2017 - 2018', 'federation': 'UEFA', 'competition_cluster': 'Spain', 'away_team': 'Real Betis', 'result': '', 'is_expired': False, 'last_update_at': '2018-04-22T14:06:35.857000'}, {'odds': {'2': 12.426, 'X': 5.661, '1X': 1.038, '12': 1.102, '1': 1.213, 'X2': 3.932}, 'home_team': 'Sporting CP', 'prediction': '1', 'status': 'pending', 'id': 13406, 'start_date': '2018-04-22T20:15:00', 'competition_name': 'Primeira Liga', 'season': '2017 - 2018', 'federation': 'UEFA', 'competition_cluster': 'Portugal', 'away_team': 'Boavista', 'result': '', 'is_expired': False, 'last_update_at': '2018-04-22T14:06:35.857000'}]}


"""

twitter_api = Twython(tokens.consumer_key, tokens.consumer_secret, tokens.access_token, tokens.access_token_secret)

# Example JSON response
json_response = {"data": [{"federation": "UEFA", "home_team": "Manchester City", "prediction": "1", "status": "pending", "season": "2017 - 2018", "start_date": "2018-04-22T16:30:00", "result": "", "odds": {"X": 8.458, "12": 1.053, "2": 20.46, "X2": 5.864, "1": 1.135, "1X": 1.013}, "id": 13249, "competition_cluster": "England", "last_update_at": "2018-04-22T14:06:35.857000", "competition_name": "Premiership", "is_expired": "false", "away_team": "Swansea"}]}

# Football prediction API
#headers = {"X-Mashape-Key": tokens.x_mashape_key, "Accept" : "application/json"}
#response = requests.get(url="https://football-prediction-api.p.mashape.com/api/v1/predictions?federation=uefa", headers=headers)
#json_response = response.json()

#print(json.dumps(json_response, indent=4))


def get_wanted_league_games_from_json(json_data):
    '''

    :param json_data: the json data returned from the API call
    :return: filtered json data with only relevant leagues
    '''
    leagues_we_want = ["premiership", "champions_league"]
    leagues_json = {}
    for data in json_data.get('data'):
        if data["competition_name"].lower() in leagues_we_want:
            print("Found a game in the {}".format(data['competition_name']), flush=True)
            leagues_json.update(data)
    get_the_relevant_information_from_previous_query(leagues_json)
    return leagues_json

def get_the_relevant_information_from_previous_query(json_data):
    competition_name = json_data["competition_name"]
    home_team = json_data["home_team"]
    away_team = json_data["away_team"]
    prediction = json_data["prediction"]
    date = json_data["start_date"]
    tweeting_relevant_data(competition_name, home_team,away_team,prediction,date)

def tweeting_relevant_data(competition_name, home_team, away_team, prediction, date):
    if prediction == "1":
        winner = home_team + " win"
    elif prediction == "X":
        winner = "Draw"
    else:
        winner = away_team + " win"

    date = format_date_time(date)

    tweet = "#{}\n\n#{} vs #{}\nKick off: {}\n\nPrediction: {} \n".format(competition_name, home_team.replace(" ", ""), away_team.replace(" ", ""), date, winner)

    #twitter_api.update_status(status=tweet)
    print("Tweet: {}".format(tweet))

def format_date_time(date_and_time):
    date = date_and_time.split("T")[0]
    time = date_and_time.split("T")[1]

    year, month, day = date.split("-")

    time = time.split(":")[0] + ":" + time.split(":")[1]

    return "{}/{}/{} {}".format(day, month, year, time)

get_wanted_league_games_from_json(json_response)