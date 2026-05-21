import requests
from API_KEY import API_KEY

# game_name = 'raynerjun'
# tag_line = 'robck'
# region = 'americas'

class MyOpgg():
    []

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
    return match_info
    
    # def get_champions():
    #     nonlocal match_info
    #     match_champions = []
    #     i = 0
    #     for player in match_info['participants']:
    #         champion = match_info['participants'][i]['championName']
    #         champion = match_info['participants'][i]['lane']
    #         match_champions.append(champion)
    #         if i < len(match_info['participants']):
    #             i += 1
    #     return match_champions
    # return get_champions()
#     def get_players(match_info):
#         match_players = []
#     #     i = 0
#     #     for player in match_info['participants']:
#     #         champion = match_info['participants'][i]['championName']
#     #         match_players.append(champion)
#     #         if i < len(match_info['participants']):
#     #             i += 1
#     #     return match_players
#     #   return get_players(match_info)
#         # return match_info['participants']
#     # get_players(match_info)

# print(get_match_players()['participants'][0]['summonerId'])
print(get_player())


# champion = match_info['participants'][i]['championName']
# lane = match_info['participants'][i]['lane']