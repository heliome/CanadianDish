from datetime import datetime
import ingredient
import pdf
import recipe
import adds

def getRecipe():
    try:

        #Check the course and give needed url string
        course = input()
        if course.lower() == "dinner" or course.lower() == "lunch":
            z = "f%5B0%5D=meal%3A46&" 
        elif course.lower() == "breakfast":
            z = "f%5B0%5D=meal%3A45&"
        elif course.lower() == "snack":
            z = "f%5B0%5D=meal%3A47&"
        else:
            return print("Error: check the name of the course")
        
        month = datetime.now().strftime('%B')

        img, name, preparation, cooking, serves, ingredients, steps, tips = recipe.rand(z)

        #Get the ingredients, that were not supposed to be used this month,
        #check if recipe has them
        nonIngredients = ingredient.ingredient(month)
        text = ""
        for i in ingredients.keys():
            for j in ingredients[i]:
                text += j + " "
        while check(nonIngredients, text):
            text = recipe.rand(z)

        #Get additional data and create pdf
        riddles, drinks = adds.add()
        pdf.create_pdf(img, name, preparation, cooking, serves, ingredients, steps, tips, riddles, drinks)
    
    except:
        print("Sorry, we have a problem, please try again later")


#function to check if there is a missing ingredient in recipe
def check(ingr, text):

    for i in ingr:
        if text.__contains__(i):
            return True
        
    return False

getRecipe()