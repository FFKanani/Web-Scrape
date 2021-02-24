import requests
from bs4 import BeautifulSoup

def scape_planetdesert(url):
    
    page_html = requests.get(url)
    html_soup = BeautifulSoup(page_html.text, 'html.parser')
    catcus_items = html_soup.find_all('div', class_="grid-product__content")
    

    headers = 'Title, Price \n'
  
    cactuslist = []

    for catcus in catcus_items:
        print(catcus)

        title=catcus.find('div', class_="grid-product__title grid-product__title--body").text
        price=catcus.find('div', class_="grid-product__price").text
        cactuslist.append([title,price])
     
    return cactuslist

    
