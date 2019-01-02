import requests
from bs4 import BeautifulSoup

#url = 'https://www.google.com'
url = "https://isthereanydeal.com"
r = requests.get(url)
r.text
print(r.content[:100])

def saveHTML(html, path):
    with open(path, 'wb') as f:
        f.write(html)
#saves html from webpage to text file "f"

saveHTML(r.content, 'google_com')

def openHTML(path):
    with open(path, 'rb') as f:
        return f.read()
    
html = openHTML('google_com')

soup = BeautifulSoup(r.content,'html.parser')

gameTitles = soup.select('div.title')
gameTitle = gameTitles[0]

title = gameTitle.select_one('div.title').text.strip()
print(title)