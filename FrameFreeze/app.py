from flask import Flask, render_template

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("home.html")

# Sudoku Game Page
@app.route("/sudoku")
def sudoku():
    return render_template("sudoku.html")

#Tennis
@app.route('/tennis')
def tennis():
    return render_template('tennis.html')

#rps
@app.route('/rps')
def rps():
    # Rock-Paper-Scissors gesture game
    return render_template('rps.html')

#Car Racing Game
@app.route('/car')
def car():
    return render_template('car.html')

#Line draw game
@app.route("/draw")
def onelinedraw():
    return render_template("draw.html")

#Colour switch game
@app.route('/colour')
def colour():
    return render_template('colour.html')

#Car Racing
@app.route('/car_race')
def temple():
    return render_template('car_race.html')

#FAQ
@app.route('/faq')
def faq():
    return render_template('FAQ.html')

#Help 
@app.route('/help')
def help():
    return render_template('help.html')


if __name__ == "__main__":
    app.run(debug=True)
