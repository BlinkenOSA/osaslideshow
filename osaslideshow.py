import os
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    json_data = open(os.path.join(os.path.dirname(__file__), "config", "slides.json"), "r")
    slides = json.load(json_data)
    return render_template('index.html', slides=slides["slides"])


if __name__ == '__main__':
    app.run()
