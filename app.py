from flask import Flask
import scraper

url_to_scrape = "https://planetdesert.com/collections/cactus"
app=Flask(__name__)

cactuslist = scraper.scape_planetdesert(url_to_scrape)
#name =["as","asd"]

@app.route('/')
def index(): 
    return '<h1>' + str(cactuslist) +'</h1>'



