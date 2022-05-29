import pandas as pd
import numpy as np
import Recommendation.Recommenders as Recommender
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/',methods=["GET"])
def index():
    return render_template('Index.html')