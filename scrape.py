import requests
from bs4 import BeautifulSoup

# lists
urls=[]

# function created
def scrape(site):

    # getting the request from url
    r = requests.get(site)
#    print(r.content)
    # converting the text
    s = BeautifulSoup(r.text,"html.parser")

    for i in s.find_all("a"):

        href = i.attrs['href']

        if href.startswith("/"):
            site = site+href
        elif href.startswith("https"):
            site = href

        print(site)

# main function
if __name__ =="__main__":

    # website to be scrape
    site="https://www.istripper.com/info/sitemap"

    # calling function
    scrape(site)
