from flask import Flask, render_template, request
import requests
from API_KEY import API_KEY


# game_name = 'raynerjun'
# tag_line = 'robck'
# region = 'americas'

class MyOpgg():
    []
    
def get_player_by_puuid(puuid):
    player_by_puuid = f'https://americas.api.riotgames.com/riot/account/v1/accounts/by-puuid/{puuid}?api_key={API_KEY}'
    player = requests.get(player_by_puuid).json()
    return f'{player['gameName']} #{player['tagLine']}'

def get_player():
    game_name = 'raynerjun'
    tag_line = 'robck'
    region = 'americas'
    
    api_url = f'https://{region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}?api_key={API_KEY}'

    player = requests.get(api_url).json()

    puuid = player['puuid']
    return puuid
    
def get_match():
    puuid = get_player()
    get_matches= f'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=20&api_key={API_KEY}'

    match_list = requests.get(get_matches).json()
    
    return match_list

def get_match_info():
    match_list = get_match()
    
    match_id = match_list[0]
    
    match = f'https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={API_KEY}'
    match_info = requests.get(match).json()['info']
    return match_info

def get_match_players():
    match_info = get_match_info()
    
    def get_champions():
        nonlocal match_info
        
        match_players = []
        i = 0
        for player in match_info['participants']:
            champion = match_info['participants'][i]['championName']
            individualPosition = match_info['participants'][i]['individualPosition']
            kills = match_info['participants'][i]['kills']
            deaths = match_info['participants'][i]['deaths']
            assists = match_info['participants'][i]['assists']
            puuid = match_info['participants'][i]['puuid']
            summonerName = get_player_by_puuid(puuid)
            # item = match_info['participants'][i]['item0']
            totalMinionsKilled = match_info['participants'][i]['totalMinionsKilled']
            match_players.append({
                'champion':f'{champion}', 
                 'individualPosition':f'{individualPosition}', 
                 'kills':f'{kills}', 
                 'deaths':f'{deaths}', 
                 'assists':f'{assists}', 
                 'summonerName':f'{summonerName}', 
                 'totalMinionsKilled':f'{totalMinionsKilled}'
                 })
            if i < len(match_info['participants']):
                i += 1
        return match_players
    return get_champions()

# print(list(get_match_players()))
