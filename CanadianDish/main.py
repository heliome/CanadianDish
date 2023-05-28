import recipe
import pdf
import adds

def getRecipe():
    try:
        #Getting the data and creating pdf
        img, name, preparation, cooking, serves, ingredients, steps, tips = recipe.rand()
        riddles, drinks = adds.add()
        pdf.create_pdf(img, name, preparation, cooking, serves, ingredients, steps, tips, riddles, drinks)
    except: 
        print("Sorry, we have a problem, please try again later")
        
getRecipe()