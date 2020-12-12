import os

from flask import (
    Flask, flash, render_template,
    redirect, request, url_for)
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
        return redirect(url_for("get_games"))

    games = list(mongo.db.games.find())
    return render_template("add_game.html", games=games)


@app.route("/edit_game/<game_id>", methods=["GET", "POST"])
def edit_game(game_id):
    if request.method == "POST":
        submit = {
            "category": request.form.get("category"),
            "game_name": request.form.get("game_name"),
            "age_range": request.form.get("age_range"),
            "number_of_players": request.form.get("number_of_players"),
            "link_to_shop": request.form.get("link_to_shop"),
            "image_url": request.form.get("image_url"),
            "description": request.form.get("description")
        }
        mongo.db.games.update({"_id": ObjectId(game_id)}, submit)
        flash("Game Successfully Updated")
        return redirect(url_for("get_games"))

    game = mongo.db.games.find_one({"_id": ObjectId(game_id)})
    return render_template("edit_game.html", game=game)


@app.route("/delete_game/<game_id>")
def delete_game(game_id):
    mongo.db.games.remove({"_id": ObjectId(game_id)})
    flash("Game Successfully Deleted")
    return redirect(url_for("get_games"))



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
