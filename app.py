from flask import Flask, request, render_template
import gamelogic


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        gamelogic.cellChange(gamelogic.turn, [(str)(request.form)[33], (str)(request.form)[34]])
        gamelogic.turnChange()
    return render_template("main.html", cells=gamelogic.cells, turn=gamelogic.turn, game=gamelogic.checkCells())
    