from bs4 import BeautifulSoup
import requests

def VegsAndFruts(soup, month, i):

    lst = []
    al = []
    main = soup.find('main').find_all("table")[i].find_all("tr")
    for row in main:
        if row.find('td', {"class": "column-1"}) != None:
            name = row.find('td', {"class": "column-1"}).text
            if name.__contains__('('):
                al.append(name.split(' ')[0])
            elif name.__contains__('and'):
                al.append(name.split(' and ')[0])
                al.append(name.split(' and ')[1])
            else:
                al.append(name)

    for row in main:
        tag = row.find('a', {"title": month})
        if tag is not None:
            name = row.find('td', {"class": "column-1"}).text
            if name.__contains__('('):
                lst.append(name.split(' ')[0])
            elif name.__contains__('and'):
                lst.append(name.split(' and ')[0])
                lst.append(name.split(' and ')[1])
            else:
                lst.append(name)

    al.pop(0)
    al = list(dict.fromkeys(al))
    lst = list(dict.fromkeys(lst))
    l3 = [x.lower() for x in al if x not in lst]
    return l3


def ingredient(month):

    url = "https://canadianfoodfocus.org/whats-in-season/"

    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")

    fruts = VegsAndFruts(soup, month, 0)
    vegs = VegsAndFruts(soup, month, 1)
    
    ingredients = fruts + vegs
    
    return ingredients