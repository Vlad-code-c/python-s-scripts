from bottle import route, run, view, request, get
from datetime import datetime as dt 
from random import random 
from random_horoscope import generate_prophecies


text = 'This is text'

@route()
def get_predictions():
    text = request("https://api.exchangerate-api.com/v4/latest/USD")
    return text


@route("/") 
@view("predictions") 
def index():   
    now = dt.now() 
 
    x = random() 
 
    predictions = get_predictions()


    return {     
      "date": f"{now.year}-{now.month}-{now.day}",     
      "predictions": predictions,     
        "special_date": x > 0.5,     
        "x": x,   
    } 
 
run(   
    host="localhost",   
    port=8880,   
    debug=True,
    autoreload=True 
)