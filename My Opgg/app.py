from flask import Flask, render_template
from lol_matches import get_match
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
    return render_template(
        'opgg.html',
        summonerName='null',
        tagLine='null',
        region='null',
        rank='null',
        gameResult='null',
        lane=player_info['individualPosition'],
        champion=player_info['champion'],
        kills=player_info['kills'],
        deaths=player_info['deaths'],
        assists=player_info['assists'],
        cs=player_info['totalMinionsKilled']
        )

if __name__ == '__main__':
    app.run(debug=True)