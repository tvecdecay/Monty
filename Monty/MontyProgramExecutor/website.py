import requests
import webbrowser

hyperspace = ["https", "http"]

class website:
    def __init__(self, optup = []):
        self.url = optup[1]
        if optup[2]:
            webbrowser.open(optup[1])
    
    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, Surl):
        try:
            self.__url = check(Surl) + "://" + Surl
        except:
            print("Please enter a valid website!")

    def open(self):
        try:
            webbrowser.open(self.url)
        except Exception as p:
            print(p)

def check(URL:str):
    for i in hyperspace:
        try:
            requests.get(i + "://" + URL)
            return i
        except:
            continue
    raise Exception("URL Error: Given string is not a website.")