from flask import Flask, render_template, abort
import json

app = Flask(__name__)

def loaddb(dbroute):
    with open(dbroute, "r", encoding="utf-8") as f:
        db = json.load(f)
    return db["datos"]

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/pokemon/<int:dex_id>")
def pokemon(dex_id):
    pokedexdb = loaddb("data/pokemondb.json")
    pokequery = next((item for item in pokedexdb if item["id"] == dex_id), None)
    if pokequery is None:
        abort(404)
    return render_template("pokemon.html", poke = pokequery)

@app.route("/pokedex/")
def pokedex():
    pokedexdb = loaddb("data/pokemondb.json")
    return render_template("pokedex.html", dex=pokedexdb, n = 386)

@app.route("/items/")
def items():
    itemdb = loaddb("data/itemdb.json")
    return render_template("items.html", items=itemdb)

@app.route("/item/<itemname>")
def item(itemname):
    itemdb = loaddb("data/itemdb.json")
    itemquery = next(i for i in itemdb if i["name"]== itemname)
    if itemquery is None:
        abort(404)
    return render_template("item.html", iteminfo = itemquery)


@app.route("/bayas/")
def bayas():
    return render_template("bayas.html")    

@app.route("/extras/")
def extras():
    return render_template("extras.html")
#@app.route("/p/<string:slug>/")
#def show_post(slug):
#    return render_template("post_view.html", slug_title=slug)
    
#@app.route("/admin/post/")
#@app.route("/admin/post/<int:post_id>")
#def post_form(post_id=None):
#    return render_template("admin/post_form.html", post_id=post_id)