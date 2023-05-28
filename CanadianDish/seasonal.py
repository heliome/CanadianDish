from datetime import datetime
import ingredient
import recipe
import pdf
import adds

def getRecipe():
    try:
        month = datetime.now().strftime('%B')

        img, name, preparation, cooking, serves, ingredients, steps, tips = recipe.rand()
        
        #Get the non-season ingredients
        nonIngredients = ingredient.ingredient(month)
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


getRecipe()

