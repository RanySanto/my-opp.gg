from flask import Flask, render_template, request
import requests
from API_KEY import API_KEY

# class MyOpgg:
#     def __init__(self, game_name, tag_line, region):
#         self.name = game_name
#         self.id = tag_line
#         self.region = region
        
#     def get_player_matches():
#         []

def set_nickname(nick):
    summonerName = ''
    tagLine = ''
    index = 0
    istagline = False
    
    for i in nick:
        if not istagline:
            if not nick[index] == '#':
                summonerName += nick[index]
                index += 1
            else:
                index += 1
                istagline = True
                continue
        else:
            tagLine += nick[index]
            index += 1
                
    return summonerName, tagLine
# precisa ser independente
def get_player_by_puuid(puuid):
        player_by_puuid = f'https://americas.api.riotgames.com/riot/account/v1/accounts/by-puuid/{puuid}?api_key={API_KEY}'
        player = requests.get(player_by_puuid).json()
        return f'{player['gameName']} #{player['tagLine']}'

# precisa ser independente
def get_player(game_name, tag_line, region): 
    api_url = f'https://{region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}?api_key={API_KEY}'
    player = requests.get(api_url).json()
    puuid = player['puuid']
    return puuid
        
def get_match(game_name, tag_line, region):
    puuid = get_player(game_name, tag_line, region)
    get_matches= f'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=20&api_key={API_KEY}'
    match_list = requests.get(get_matches).json()
    match_history = []
    match = f'https://americas.api.riotgames.com/lol/match/v5/matches/{match_list[0]}?api_key={API_KEY}'
    match_info = requests.get(match).json()['info']
    blueTeamWin = match_info['teams'][0]['win']
    redTeamWin = match_info['teams'][1]['win']
    
    i = 0
    for match in match_list:
        match = f'https://americas.api.riotgames.com/lol/match/v5/matches/{match_list[i]}?api_key={API_KEY}'
        match_info = requests.get(match).json()['info']
        match_history.append(get_players_info(match_info))
        # match_history.append(match_info)
        i += 1
    return match_history
        
def get_players_info(match_info):
    match_players = []
    i = 0
    # gameResult = match_info[i]['endOfGameResult']
    # 'gameResult':f'{gameResult}'
    for player in match_info['participants']:
        champion = match_info['participants'][i]['championName']
        individualPosition = match_info['participants'][i]['individualPosition']
        kills = match_info['participants'][i]['kills']
        deaths = match_info['participants'][i]['deaths']
        assists = match_info['participants'][i]['assists']
        puuid = match_info['participants'][i]['puuid']
        # summonerName = get_player_by_puuid(puuid)
        # if not puuid == False:
        #     summonerName = get_player_by_puuid(puuid)
        # else:
        #     summonerName = champion
        # item = match_info['participants'][i]['item0']
        riotIdGameName = match_info['participants'][i]['riotIdGameName']
        riotIdTagLine = match_info['participants'][i]['riotIdTagline']
        totalMinionsKilled = match_info['participants'][i]['totalMinionsKilled']
        match_players.append({
            'champion':f'{champion}', 
            'individualPosition':f'{individualPosition}', 
            'kills':f'{kills}', 
            'deaths':f'{deaths}', 
            'assists':f'{assists}', 
            # 'summonerName':f'{summonerName}',
            'riotIdGameName':f'{riotIdGameName}#{riotIdTagLine}',
            'totalMinionsKilled':f'{totalMinionsKilled}',
            
            })
        if i < len(match_info['participants']):
            i += 1
    return match_players

# def get_search_player_info(match_info):

nick = input('Type your nick\n')
nickname = set_nickname(nick)[0]
tagline = set_nickname(nick)[1]
# print(nickname, tagline)

# get each champion and info for the first 20 matches of the player
player_info = get_match(nickname, tagline, 'americas')

def get_search_player_info(player_info):
    player_scores = []
    i = 0
    for match in player_info:
        i = 0
        if not player_info[i]['riotIdGameName'] == 'RaynerJun#robck':
            i += 1
            continue
        else:
            player_scores.append(player_info[i])
            i+=1
    
    return player_scores
    
print(get_search_player_info(player_info))


# print(get_player_by_puuid('59Noj7T2aklO7Og0dHpIdLAQ0sUE22Af8O8gtKzGbTvgiiYy4BQAPTx1-EtMxZSgsQG9qkZFr9pYeA'))

# print(get_search_player_info(get_match(nickname, tagline, 'americas')))