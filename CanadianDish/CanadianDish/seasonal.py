from datetime import datetime
from . import ingredient
from . import recipe
from . import pdf
from . import adds

def getSeasonRecipe(month = ""):

    
    try:
        img, name, preparation, cooking, serves, ingredients, steps, tips = recipe.rand()


        #Get the non-season ingredients
        if month == "":
            month = datetime.now().strftime('%B')
            nonIngredients = ingredient.ingredient(month)
        else:
        
            nonIngredients = ingredient.ingredient(month.capitalize())
            if len(nonIngredients)==37:
                return print("Error: check the name of season")

        text = ""
        for i in ingredients.keys():
            for j in ingredients[i]:
                text += j + " "

        #check if the recipe has them
        while check(nonIngredients, text):
            text = recipe.rand()

        #Add data and do a pdf
        riddles, drinks = adds.add()
        pdf.create_pdf(img, name, preparation, cooking, serves, ingredients, steps, tips, riddles, drinks)
    except:
        print("Sorry, we have a problem, please try again later")

def check(ingr, text):

    for i in ingr:
        if text.__contains__(i):
            return True
        
    return False

def main():
    getSeasonRecipe()

if __name__=="__main__":
    main()
