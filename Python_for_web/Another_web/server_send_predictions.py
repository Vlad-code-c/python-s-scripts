from bottle import route, run, view 
from datetime import datetime as dt 
from random import random 
from random_horoscope import generate_prophecies

#@view("predictions") 
@route("/api/forecasts") 
def index():   
    now = dt.now() 
 
    x = random() 
 
    predictions = generate_prophecies()

    return { "predictions": predictions } 
 
run(   
    host="localhost",   
    port=8080,   
    autoreload=True 
)