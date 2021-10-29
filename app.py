from flask import Flask, request, render_template
import gamelogic


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

gamelogic.start()

@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        print((str)(request.form))
        if "cell-button" in (str)(request.form):
            gamelogic.cellChange(gamelogic.turn, [(str)(request.form)[34], (str)(request.form)[35]])
            gamelogic.turnChange()
        elif "play-again-button" in (str)(request.form):
            gamelogic.start()
    return render_template("main.html", cells=gamelogic.cells, turn=gamelogic.turn, game=gamelogic.checkCells())
    