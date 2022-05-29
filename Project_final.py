import pandas as pd
import numpy as np
import Recommendation.Recommenders as Recommender
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/',methods=["GET"])
def index():
    return render_template('Index.html')

@app.route('/MAIN',methods=["POST"])
def my_form():
    #Fetching the data set
    df_1 = pd.read_csv('triplets_file.csv')
    df_2 = pd.read_csv('song_data.csv')
    #Merging Both data sets
    final_df = df_1.merge(df_2, on = 'song_id')
    #Essentially Aggregating count for a particular song from  the entire user set
    final_df['song'] = final_df['title']+' - '+final_df['artist_name']
    first_name=request.form.get("fname")
    last_name=request.form.get("lname")
    userid=int(request.form.get("userid"))
    pr = Recommender.pop_recommend()
    pr.create(final_df, 'user_id', 'song')
    #Storing the top ten songs with most counts in a list
    last=pr.recommend(final_df['user_id'][userid])
    x = []
    for song in last['song'][0:10]:
        x.append(song)
    
    return render_template('MAIN.html',s=x)
@app.route('/login',methods=["GET"])
def login():
    return render_template('Login.html')
@app.route('/Registration',methods=["GET"])
def Registration():
    return render_template('Registration.html')
@app.route('/Pricing',methods=["GET"])
def Pricing():
    return render_template('Pricing.html') 
@app.route('/user',methods=["GET"])
def user():
    return render_template('user.html')         

app.run();

