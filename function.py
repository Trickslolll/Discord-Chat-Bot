import requests
from bs4 import BeautifulSoup


def check_status(url):  # check if there is item on sale on the website
    target = requests.get(url)
    soup = BeautifulSoup(target.text, "html.parser")
    result = soup.find_all("div", class_="as-price-currentprice as-producttile-currentprice")

    if len(result) == 0:
        return False
    else:
        return True
