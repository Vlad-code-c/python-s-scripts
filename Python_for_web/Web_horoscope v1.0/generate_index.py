#coding: utf-8
from random_horoscope import generate_prophecies 
from random_horoscope import times, advices, promises
from datetime import datetime as dt 

#GENERATE index.html:
def generate_link(title, href):
    link = f"\n<a href='{href}'><p>{title}</p></a>"
    return link

def generate_page(head, body, link):  
    page = f"<html>{head}{body}{link}</html>"  
    return page 

def generate_head(title):  
    head = f"""<head>
    <meta charset='utf-8'>
    <title>{title}</title>
    """  
    return head 

def generate_body(header, paragraphs):  
    body = f"<h1>{header}</h1>"    
    for p in paragraphs:
        body = body + f"<p>{p}</p>"   
    return f"<body>{body}</body>" 

def save_page(title, header, paragraphs, output="index.html"):  
    fp = open(output, "w")  
    today = dt.now().date()  
    page = generate_page(   
            head=generate_head(title),   
            body=generate_body(
                    header=header, 
                    paragraphs=paragraphs),
            link=generate_link(title="About", href="about.html") 
    )
    print(page, file=fp)  
    fp.close()


today = dt.now().date() 
save_page(     
    title="Horoscope for today: ", 
    header="Day " + str(today) + ":",     
    paragraphs=generate_prophecies(), 
    )


#GENERATE about.html
def generate_body_about(header):
    body = f"<h1>{header}</h1>" 
    body += "<p>1. Times:</p><ul style='list-style-type:circle'>"
    for x in range(len(times)):
        body += f"<li>{times[x]}</li>\n"
    body += "</ul>"
    
    body += "<p>2. Advices:</p><ul style='list-style-type:circle'>"
    for x in range(len(advices)):
        body += f"<li>{advices[x]}</li>\n"
    body += "</ul>"

    body += "<p>3. Promises:</p><ul style='list-style-type:circle'>"
    for x in range(len(promises)):
        body += f"<li>{promises[x]}</li>\n"
    body += "</ul>"

    return f"<body>{body}</body>" 

def image_get(url, alt=''):
    image = f"<img src='{url}' alt='{alt}' height='100' width='100'>"
    return image

def generate_page_about(head, img, body, link):  
    page = f"<html>{head}{body}{link}</html>"  
    return page 

def save_page_about(title, img, header, output="about.html"):  
    fp = open(output, "w")  
    today = dt.now().date()  
    page = generate_page_about(   
            head=generate_head(title),   
            img=image_get(url="https://i.imgur.com/8kxxoqS.jpg", alt="Horoscope"),
            body=generate_body_about(header),
            link=generate_link(title="Home", href="index.html") 
    )
    print(page, file=fp)  
    fp.close()

save_page_about(     
    title="About all",
    img="https://i.imgur.com/8kxxoqS.jpg",
    header="Day " + str(today) + ":"
    )