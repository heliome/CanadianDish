import requests
from bs4 import BeautifulSoup
import random

def rand(n=""):
    #Function to start
    #Gets the random page from thesite with food

    url = f"https://food-guide.canada.ca/en/recipes/?{n}page=0"

    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")
    nav = soup.find("ul",{"class":"pagination js-pager__items"}).find_all("li")
    k = random.randint(0,len(nav)-2)
    return meal(k)


def meal(k, n=""):
    #Gets random dish from the page
    url = f"https://food-guide.canada.ca/en/recipes/?{n}page={k}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")
    main = soup.find_all("div",{"class":"views-field views-field-field-featured-image"})
    k = random.randint(0,len(main)-1)
    site = main[k].find("a")["href"]
    return about(site)

def about(site):
    #Gets all the data about recipe
    url = f"https://food-guide.canada.ca{site}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")
    #Get name
    main = soup.find("h1",{"class":"page_text"})
    name = main.text

    #Get preparation data
    prep = []
    main = soup.find("div",{"class":"recipe-prep-information row"}).find_all("div",{"class":"item"})
    for i in main:
        i = i.find_all("div")
        prep.append(i[0].text.split("\n")[2])

    #Get ingredients
    ingredients = dict()
    main = soup.find("section",{"class":"block block-ctools-block block-entity-fieldnodefield-ingredients clearfix"})
    ingr = main.find_all("ul")
    bonus = main.find_all('p')

    for i in range(len(bonus)-1):
        if bonus[i].text == "" or bonus[i].text == " ":
            bonus.pop(i)
    if len(ingr) == len(bonus):
        s=0
        for i in bonus:
            k = ingr[s].text.replace(u'\xa0', u' ').replace("⅓", "1/3").replace("⅔", "2/3").split("\n")
            k.pop(-1)
            ingredients[i] = k
            s +=1
    else:
        k = ingr[0].text.replace(u'\xa0', u' ').replace("⅓", "1/3").replace("⅔", "2/3").split("\n")
        k.pop(-1)
        ingredients["Ingredients"] = k

        if bonus != None:
            s=1
            for i in bonus:
                k = ingr[s].text.replace(u'\xa0', u' ').replace("⅓", "1/3").replace("⅔", "2/3").split("\n")
                k.pop(-1)
                ingredients[i] = k
                s +=1
    
    
    #Get all the steps
    steps = []
    main = soup.find("section",{"class":"block block-ctools-block block-entity-fieldnodefield-directions clearfix"})
    main = main.text.split("\n")
    for i in main:
        steps.append(i.replace(u'\xa0', u' '))
    for i in range(2):
        steps.pop(0)
        steps.pop(-1)

    #Get all tips
    tips=[]
    main = soup.find("div",{"class":"field field--name-field-cooking-tips field--type-text-long field--label-above"})
    main = main.text.split("\n")
    for i in main:
        if not (i.lower().__contains__("kid") or i.lower().__contains__("child") or i.lower().__contains__("chef") or i.lower().__contains__("little")):
           tips.append(i)
    for i in range(2):
        tips.pop(0)
        tips.pop(-1)

    #Get tips
    img = soup.find("div",{"class":"featured-image-wrapper"}).find("img")["src"]
    data = requests.get(img).content
    f = open("img.jpg",'wb')
    f.write(data)
    f.close()
    
    

    return "img.jpg", name, prep[0], prep[1], prep[2], ingredients, steps, tips



