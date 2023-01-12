#!/usr/bin/env python

from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify

app= Flask(__name__)

marvel_villains = [{
    "name": "Red Skull",
    "trivia": "Unlike his comic book counterpart who has a mask, this version of Red Skull's appearance is biological, due to him ingesting a version of the Super-Soldier Serum",
    "quote":"You could have the power of the gods! Yet you wear a flag on your chest and think you fight a battle of nations! I have seen the future, Captain! There are no flags!",
    ""
     "powers": [
        "enhanced strength",
        "enhanced mobility",
        "enhanced endurance",
        "accelerated healing",
        "enhanced intelligence"
              ]
             }]

@app.route("/")
def index():
    # jsonify returns legal JSON
    return jsonify(marvel_villains)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
