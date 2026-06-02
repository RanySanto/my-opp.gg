from flask import Flask, render_template, request
from lol_matches import get_match
from lol_matches import set_nickname
from lol_matches import get_search_player_info
from lol_matches import get_player
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route("/")
def opgg():
    nick = request.args.get('nick')
    # get just the info of the player of the last 20 matches
    playerGames = get_search_player_info(get_match(get_player(set_nickname(nick)[0], set_nickname(nick)[1], 'americas')))
    flat_list = [game[0] for game in playerGames]
    tagLine = set_nickname(nick)[1]
    
    return render_template(
        'opgg.html', 
        flat_list = flat_list,
        summonerName=flat_list[0]['riotIdGameName'],
        tagLine=tagLine,
        rank='Platinum',
        lp='23'
        )
                           

if __name__ == "__main__":
    # serve(app, host="0.0.0.0", port=8000)
    app.run(debug=True)
    
# Start app:
# activate
# python3 app.py 