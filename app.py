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
    games = list(mongo.db.games.find().sort("_id", -1).limit(3))
    return render_template("home.html", games=games)


@app.route("/games")
def games():
    games = list(mongo.db.games.find().sort("game_name"))
    return render_template("games.html", games=games)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        game = {
            "category_name": request.form.get("category_name"),
            "game_name": request.form.get("game_name"),
            "age_range": request.form.get("age_range"),
            "number_of_players": request.form.get("number_of_players"),
            "link_to_shop": request.form.get("link_to_shop"),
            "image_url": request.form.get("image_url"),
            "description": request.form.get("description")
        }
        mongo.db.games.insert_one(game)
        flash("Game Successfully Added")
        return redirect(url_for("games"))

    categories = mongo.db.categories.find()
    return render_template("add.html", categories=categories)


@app.route("/edit/<game_id>", methods=["GET", "POST"])
def edit(game_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "game_name": request.form.get("game_name"),
            "age_range": request.form.get("age_range"),
            "number_of_players": request.form.get("number_of_players"),
            "link_to_shop": request.form.get("link_to_shop"),
            "image_url": request.form.get("image_url"),
            "description": request.form.get("description")
        }
        mongo.db.games.update({"_id": ObjectId(game_id)}, submit)
        flash("Game Successfully Updated")
        return redirect(url_for("games"))

    game = mongo.db.games.find_one({"_id": ObjectId(game_id)})
    categories = mongo.db.categories.find()
    return render_template("edit.html", game=game, categories=categories)


@app.route("/delete/<game_id>")
def delete(game_id):
    mongo.db.games.remove({"_id": ObjectId(game_id)})
    flash("Game Successfully Deleted")
    return redirect(url_for("games"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
