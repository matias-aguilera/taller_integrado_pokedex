from flask import Flask, render_template, abort
import json

app = Flask(__name__)

def loaddb():
    with open("data/pokemondb.json", "r", encoding="utf-8") as f:
        pokedb = json.load(f)
    return pokedb["datos"]

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/prev/<int:dex_id>")
def poke_prev(dex_id):
    pokedexdb = loaddb()
    pokequery = next((item for item in pokedexdb if item["id"] == dex_id), None)
    if pokequery is None:
        abort(404)
    return render_template("poke_prev.html", poke = pokequery)

@app.route("/pokedex/")
def pokedex():
    pokedexdb = loaddb()
    return render_template("pokedex.html", dex=pokedexdb, n = 12)

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