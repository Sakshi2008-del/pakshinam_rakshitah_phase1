from flask import Flask, render_template, jsonify
import random
import numpy as np
from datetime import datetime

app = Flask(__name__)

# --------------------------
# Radiation Generator
# --------------------------
def generate_radiation():
    solar = round(random.uniform(300, 1200), 2)
    human = round(random.uniform(0.5, 5.0), 2)
    rss = round((solar * 0.002) + (human * 2), 2)
    return solar, human, rss


# --------------------------
# Birds Data
# --------------------------
birds = {
    "Sparrow": {"multiplier":1.1,"problem":"Feather stress","precaution":"Provide shaded nests","image":"https://upload.wikimedia.org/wikipedia/commons/0/0e/Passer_domesticus_male.jpg"},
    "Pigeon": {"multiplier":1.3,"problem":"Eye irritation","precaution":"Urban EMF control","image":"https://upload.wikimedia.org/wikipedia/commons/1/1e/Feral_pigeon.jpg"},
    "Crow": {"multiplier":1.5,"problem":"Behavior shift","precaution":"Reduce tower radiation","image":"https://upload.wikimedia.org/wikipedia/commons/0/0a/Corvus_brachyrhynchos_2.jpg"},
    "Peacock": {"multiplier":1.2,"problem":"Feather dullness","precaution":"Limit open exposure","image":"https://upload.wikimedia.org/wikipedia/commons/1/15/Peacock_Plumage.jpg"},
    "Parrot": {"multiplier":1.4,"problem":"Reproductive stress","precaution":"Green habitat zones","image":"https://upload.wikimedia.org/wikipedia/commons/4/4e/Parrot.jpg"},
    "Owl": {"multiplier":1.6,"problem":"Vision disturbance","precaution":"Forest protection","image":"https://upload.wikimedia.org/wikipedia/commons/1/1e/Owl.jpg"},
    "Eagle": {"multiplier":1.8,"problem":"DNA mutation risk","precaution":"Continuous monitoring","image":"https://upload.wikimedia.org/wikipedia/commons/1/19/Bald_Eagle.jpg"},
    "Kingfisher": {"multiplier":1.25,"problem":"Skin sensitivity","precaution":"Water shielding","image":"https://upload.wikimedia.org/wikipedia/commons/3/32/Common_Kingfisher.jpg"},
    "Flamingo": {"multiplier":1.35,"problem":"Metabolic disruption","precaution":"Wetland care","image":"https://upload.wikimedia.org/wikipedia/commons/8/84/Flamingos_Laguna_Colorada.jpg"},
    "Woodpecker": {"multiplier":1.45,"problem":"Neuro stress","precaution":"Reduce EM waves","image":"https://upload.wikimedia.org/wikipedia/commons/9/91/Woodpecker.jpg"}
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/radiation")
def radiation():
    solar, human, rss = generate_radiation()

    bird_data = []
    for name, data in birds.items():
        risk = round(rss * data["multiplier"], 2)
        bird_data.append({
            "name": name,
            "risk": risk,
            "problem": data["problem"],
            "precaution": data["precaution"],
            "image": data["image"]
        })

    return jsonify({
        "solar": solar,
        "human": human,
        "rss": rss,
        "birds": bird_data
    })


@app.route("/predict")
def predict():
    solar, human, rss = generate_radiation()

    past = round(rss - random.uniform(1,3),2)
    future1 = round(rss + random.uniform(1,3),2)
    future2 = round(future1 + random.uniform(1,2),2)

    return jsonify({
        "past": past,
        "present": rss,
        "future1": future1,
        "future2": future2
    })


if __name__ == "__main__":
    app.run(debug=True)
