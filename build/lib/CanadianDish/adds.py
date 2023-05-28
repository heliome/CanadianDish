import requests
import random

#Used to add additional thngs to the pdf
def add():
    try:
        drinks = drink()
        riddles = riddle()

        return riddles, drinks
    except:
        return print("Sorry, we have a problem, please try again later")

#Adds drinks
def drink():
    url = "https://the-cocktail-db.p.rapidapi.com/filter.php"

    headers = {
	    "X-RapidAPI-Key": "7c3c2ba954mshc3eb9844cf76b7bp16318djsn31d3d6f4cf02",
	    "X-RapidAPI-Host": "the-cocktail-db.p.rapidapi.com"
    }
    querystring1 = {"a":"Alcoholic"}
    querystring2 = {"a":"Non-Alcoholic"}

    #Get two responses for alcoholic and non-alcoholic drinks
    alcoholic = requests.get(url, headers=headers, params=querystring1).json()
    nonalcoholic = requests.get(url, headers=headers, params=querystring2).json()
    drinks = {"Alcoholic" : [], "Non-Alcoholic" : []}

    #Find random 3 drinks for each category
    for i in range(3):
        drinks["Alcoholic"].append(alcoholic["drinks"][random.randint(0, len(alcoholic["drinks"])-1)]["strDrink"])
        drinks["Non-Alcoholic"].append(alcoholic["drinks"][random.randint(0, len(nonalcoholic["drinks"])-1)]["strDrink"])
    return drinks

#Adds riddles
def riddle():
    api_url = 'https://api.api-ninjas.com/v1/riddles?limit={}'.format("5")
    response = requests.get(api_url, headers={'X-Api-Key': 'OJUML8M6ln6VsVlrsPSHWA==304ZCHwvsuGeRX2m'})
    data = response.json()
    output = dict()
    
    # get all of data from riddles
    for i in range(len(data)-1):
        output[data[i]["title"]] = [data[i]["question"], data[i]['answer']]
    return output
    