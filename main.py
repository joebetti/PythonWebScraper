import requests

url = "https://glock.photo/yidi"
r = requests(url)
print(r.content[:100])

def saveHTML(html,path):
    with open(path,"wb") as f:
        f.write(html)
#saves html from webpage to text file "f"

saveHTML(r.content, "google.com")

def openHTML(path):
    with open(path, "rb") as f:
        return f.read()

html = openHTML("google.com")