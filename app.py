from flask import Flask, request, render_template
import gamelogic


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/", methods=['GET', 'POST'])
def main():
    turn = True
    if request.method == 'POST':
        buttonPressed = (str)(request.form)[33], (str)(request.form)[34]
        gamelogic.cells[(int)(buttonPressed[0])][(int)(buttonPressed[1])] == "o"
        print(buttonPressed)
    return render_template("main.html", cells=gamelogic.cells, turn=turn)
    