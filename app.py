from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/pokedex/")
def pokedex():
    with open("data/pokemondb.json", "r", encoding="utf-8") as f:
        pokedexdb = json.load(f)
    return render_template("pokedex.html", dex=pokedexdb, n = 6)

@app.route("/items/")
def items():
    return render_template("items.html")

@app.route("/poke/")
def pokemon():
    return render_template("pokemon.html")

#@app.route("/p/<string:slug>/")
#def show_post(slug):
#    return render_template("post_view.html", slug_title=slug)
    
#@app.route("/admin/post/")
#@app.route("/admin/post/<int:post_id>")
#def post_form(post_id=None):
#    return render_template("admin/post_form.html", post_id=post_id)