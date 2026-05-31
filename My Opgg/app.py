from flask import Flask, render_template, request
from lol_matches import get_match
from lol_matches import set_nickname
from lol_matches import get_search_player_info
from lol_matches import get_player
from waitress import serve

app = Flask(__name__)

# @app.route('/')
# def index():
#     player_info = get_match('raynerjun', 'robck', 'americas')
#     return render_template(
#         'index.html',
#          champion=player_info['champion'],                  
#



# @app.route('/')
# @app.route('/index')
# def index():
#     return render_template('index.html')

# @app.route('/opgg')
# def opgg():
#     nick = request.args.get('nick')
#     player = get_search_player_info(get_match(get_player(set_nickname(nick)[0], set_nickname(nick)[1], 'americas')))
    
#     return render_template(
#         'opgg.html',
#         summonerName=player[0][0]['riotIdGameName'],
#         rank='null',
#         gameResult='null',
#         lane=player[0][0]['individualPosition'],
#         champion=player[0][0]['champion'],
#         kills=player[0][0]['kills'],
#         deaths=player[0][0]['deaths'],
#         assists=player[0][0]['assists'],
#         cs=player[0][0]['totalMinionsKilled']
#         )
# @app.route('/test')
# def test():
#     nick = request.args.get('nick')
#     # if not bool(nick.strip()):
#     #     nick = 'raynerjun#robck'
#     # player_info = get_match(set_nickname(nick)[0], set_nickname(nick)[1], 'americas')
#     # player_info = get_match('raynerjun', 'robck', 'americas')
#     player = get_search_player_info(get_match(get_player(set_nickname(nick)[0], set_nickname(nick)[1], 'americas')))
#     # player_info = get_match('htJB8DoiRggaS9czItzaSQdRUofuWVz0I7TrBHV6QKtB26ln1cHB_w2AZE41hVK877xZHcRBGUGhFw')
    
#     # player_match_history = get_search_player_info(player_info)
    
#     return render_template(
#         'test.html',
#         summonerName=player[0][0]['riotIdGameName'],
#         rank='null',
#         gameResult='null',
#         lane=player[0][0]['individualPosition'],
#         champion=player[0][0]['champion'],
#         kills=player[0][0]['kills'],
#         deaths=player[0][0]['deaths'],
#         assists=player[0][0]['assists'],
#         cs=player[0][0]['totalMinionsKilled']
#         )
    
    
@app.route("/")
def jinja_test():
    # nick = request.args.get('nick')
    nick = 'raynerjun#robck'
    
    # send nickname then split in two then get puuid
    # player = get_player(set_nickname(nick)[0], set_nickname(nick)[1], 'americas')
    
    # get the info of all players of the last 20 matches of the given player
    # player = get_match(get_player(set_nickname(nick)[0], set_nickname(nick)[1], 'americas'))
    
    # get just the info of the player of the last 20 matches
    player = get_search_player_info(get_match(get_player(set_nickname(nick)[0], set_nickname(nick)[1], 'americas')))
    
    return render_template(
        'jinjatest.html', 
        nick = player
        # my_string="Include Help!", 
        # my_list=[player],
        # summonerName=player['riotIdGameName'],
        # rank='null',
        # gameResult='null',
        # lane=player['individualPosition'],
        # champion=player['champion'],
        # kills=player['kills'],
        # deaths=player['deaths'],
        # assists=player['assists'],
        # cs=player['totalMinionsKilled']
        )
                           

if __name__ == "__main__":
    # serve(app, host="0.0.0.0", port=8000)
    app.run(debug=True)
    
# Start app:
# activate
# python3 app.py 