from datetime import datetime
from CanadianDish import ingredient
from CanadianDish import pdf
from CanadianDish import recipe
from CanadianDish import adds

def getCombinedRecipe(course, month=""):
    

    #Check the course and give needed url string
    if course.lower() == "dinner" or course.lower() == "lunch":
        z = "f%5B0%5D=meal%3A46&" 
    elif course.lower() == "breakfast":
        z = "f%5B0%5D=meal%3A45&"
    elif course.lower() == "snack":
        z = "f%5B0%5D=meal%3A47&"
    else:
        return print("Error: check the name of the course")

    try:
        #Get the ingredients, that were not supposed to be used this month,
        #check if recipe has them

        if month == "":
            month = datetime.now().strftime('%B')
            nonIngredients = ingredient.ingredient(month)
        else:
            nonIngredients = ingredient.ingredient(month.capitalize())
            if len(nonIngredients)==37:
                return print("Error: check the name of season")

        img, name, preparation, cooking, serves, ingredients, steps, tips = recipe.rand(z)

        
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

def main():
    getCombinedRecipe()

if __name__=="__main__":
    main()