from flask import Flask, render_template
from lol_matches import get_match
from lol_matches import get_search_player_info
# import lol_matches

app = Flask(__name__)

# @app.route('/')
# def index():
#     player_info = get_match('raynerjun', 'robck', 'americas')
#     return render_template(
#         'index.html',
#          champion=player_info['champion'],                  
#                            )

@app.route('/')
def opgg():
    player_info = get_match('raynerjun', 'robck', 'americas')
    player_match_history = get_search_player_info(player_info)
    
    return render_template(
        'opgg.html',
        summonerName=player_match_history[0][0]['riotIdGameName'],
        rank='null',
        gameResult='null',
        lane=player_match_history[0][0]['individualPosition'],
        champion=player_match_history[0][0]['champion'],
        kills=player_match_history[0][0]['kills'],
        deaths=player_match_history[0][0]['deaths'],
        assists=player_match_history[0][0]['assists'],
        cs=player_match_history[0][0]['totalMinionsKilled']
        )

if __name__ == '__main__':
    app.run(debug=True)