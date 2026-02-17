from flask import Flask, render_template, request, jsonify
from game_engine import GameSession

app = Flask(__name__)

sessions = {}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/start', methods=['POST'])
def start():
    name = request.form['name']
    session = GameSession(name)
    sessions[name] = session
    return render_template("loading.html", name=name)

@app.route('/game/<name>')
def game(name):
    session = sessions[name]
    return render_template("game.html",
                           url=session.get_current_question(),
                           player=name,
                           q=session.current+1)

@app.route('/answer', methods=['POST'])
def answer():
    name = request.json["name"]
    ans = request.json["answer"]

    session = sessions[name]
    correct = session.check_answer(ans)

    if session.finished():
        return jsonify({"finished":True})

    return jsonify({
        "finished":False,
        "correct":correct,
        "next":session.get_current_question(),
        "q":session.current+1
    })

@app.route('/result/<name>')
def result(name):
    session = sessions[name]
    return render_template("result.html",
                           player=name,
                           score=session.score,
                           acc=session.accuracy())

if __name__ == "__main__":
    app.run(debug=True)
