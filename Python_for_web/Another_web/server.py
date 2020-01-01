from bottle import route, run, view, request, get
from datetime import datetime as dt 
from random import random 
from random_horoscope import generate_prophecies


text = 'this is text'
@get("/api/forecasts")
def get_predictions():
    text = request.query.predictions
    return text


@route("/") 
@view("predictions") 
def index():   
    now = dt.now() 
 
    x = random() 
 
    predictions = text


    return {     
      "date": f"{now.year}-{now.month}-{now.day}",     
      "predictions": predictions,     
        "special_date": x > 0.5,     
        "x": x,   
    } 
 
run(   
    host="localhost",   
    port=8888,   
    debug=True,
    autoreload=True 
)