import requests
from bs4 import BeautifulSoup


def get_html(URL):
    resp = requests.get(URL)
    soup = BeautifulSoup(resp.text, "lxml")
    with open("index.html", 'w') as f:
        f.write(soup.prettify())


if __name__ == '__main__':
    get_html(input("URL : "))