import random

times = ["morning", "afternoon", "evening", "night", "bedtime"]
advices = ["expect", "beware", "be open to"]
promises = ["guests from a forgotten past", "meetings with old friends",
            "unexpected holiday", "pleasant changes"]


def generate_prophecies(total_num=5, num_sentences=3):     
    prophecies = [] 
 
    for i in range(total_num):         
        forecast = ""         
        for j in range(num_sentences):             
            t = random.choice(times) 
            a = random.choice(advices)             
            p = random.choice(promises) 
 
            full_sentence = f"{t.title()} {a} {p}."             
            if j != num_sentences - 1:                 
                full_sentence = full_sentence + " " 
 
            forecast = forecast + full_sentence 
 
        prophecies.append(forecast) 
 
    return prophecies