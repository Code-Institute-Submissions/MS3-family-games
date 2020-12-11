import os

from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    games = list(mongo.db.games.find())
    return render_template("home.html", games=games)


@app.route("/get_games")
def get_games():
    games = list(mongo.db.games.find())
    return render_template("games.html", games=games)


@app.route("/add_game", methods=["GET", "POST"])
def add_game():
    if request.method == "POST":
        game = {
            "category": request.form.get("category"),
            "game_name": request.form.get("game_name"),
            "age_range": request.form.get("age_range"),
            "number_of_players": request.form.get("number_of_players"),
            "link_to_shop": request.form.get("link_to_shop"),
            "image_url": request.form.get("image_url"),
            "description": request.form.get("description")
        }
        mongo.db.games.insert_one(game)
        flash("Game Successfully Added")
        return redirect(url_for("home"))

    games = list(mongo.db.games.find())
    return render_template("add_game.html", games=games)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
