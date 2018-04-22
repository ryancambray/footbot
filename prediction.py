from twython import Twython
import requests
import json
import tokens

"""
example response

{"data": [
    {"federation": "UEFA", "home_team": "Manchester City", "prediction": "1", "status": "pending", "season": "2017 - 2018", "start_date": "2018-04-22T16:30:00", "result": "", 
    "odds": {"X": 8.458, "12": 1.053, "2": 20.46, "X2": 5.864, "1": 1.135, "1X": 1.013}, "id": 13249, "competition_cluster": "England", 
    "last_update_at": "2018-04-22T14:06:35.857000", "competition_name": "Premiership", "is_expired": false, "away_team": "Swansea"}]}

{'data': [{'odds': {'2': 6.37, 'X': 3.911, '1X': 1.113, '12': 1.213, '1': 1.553, 'X2': 2.466}, 'home_team': 'Atletico Madrid', 'prediction': '1', 'status': 'pending', 'id': 13287, 'start_date': '2018-04-22T19:45:00', 'competition_name': 'Primera Division', 'season': '2017 - 2018', 'federation': 'UEFA', 'competition_cluster': 'Spain', 'away_team': 'Real Betis', 'result': '', 'is_expired': False, 'last_update_at': '2018-04-22T14:06:35.857000'}, {'odds': {'2': 12.426, 'X': 5.661, '1X': 1.038, '12': 1.102, '1': 1.213, 'X2': 3.932}, 'home_team': 'Sporting CP', 'prediction': '1', 'status': 'pending', 'id': 13406, 'start_date': '2018-04-22T20:15:00', 'competition_name': 'Primeira Liga', 'season': '2017 - 2018', 'federation': 'UEFA', 'competition_cluster': 'Portugal', 'away_team': 'Boavista', 'result': '', 'is_expired': False, 'last_update_at': '2018-04-22T14:06:35.857000'}]}


"""

json_response = {'data': [{'odds': {'2': 6.37, 'X': 3.911, '1X': 1.113, '12': 1.213, '1': 1.553, 'X2': 2.466}, 'home_team': 'Atletico Madrid', 'prediction': '1', 'status': 'pending', 'id': 13287, 'start_date': '2018-04-22T19:45:00', 'competition_name': 'Primera Division', 'season': '2017 - 2018', 'federation': 'UEFA', 'competition_cluster': 'Spain', 'away_team': 'Real Betis', 'result': '', 'is_expired': False, 'last_update_at': '2018-04-22T14:06:35.857000'}, {'odds': {'2': 12.426, 'X': 5.661, '1X': 1.038, '12': 1.102, '1': 1.213, 'X2': 3.932}, 'home_team': 'Sporting CP', 'prediction': '1', 'status': 'pending', 'id': 13406, 'start_date': '2018-04-22T20:15:00', 'competition_name': 'Primeira Liga', 'season': '2017 - 2018', 'federation': 'UEFA', 'competition_cluster': 'Portugal', 'away_team': 'Boavista', 'result': '', 'is_expired': False, 'last_update_at': '2018-04-22T14:06:35.857000'}]}


headers = {"X-Mashape-Key": tokens.x_mashape_key, "Accept" : "application/json"}
response = requests.get(url="https://football-prediction-api.p.mashape.com/api/v1/predictions?federation=uefa", headers=headers)
#json_response = response.json()

#print(json.dumps(json_response, indent=4))


def get_wanted_league_games_from_json(json_data):
    '''

    :param json_data: the json data returned from the API call
    :return: filtered json data with only relevant leagues
    '''
    leagues_we_want = ["premiership"]
    for data in json_data.get('data'):
        leagues_json = {}
        if data["competition_name"].lower() in leagues_we_want:
            leagues_json.update()
    return leagues_json

