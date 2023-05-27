from datetime import datetime
import ingredients
import recipe

def season():
    
    month = datetime.now().strftime('%B')

    ingr = ingredients.ingredient(month)

    text = recipe.rand()
    while check(ingr, text):
        text = recipe.rand()
    print(text)
    

def check(ingr, text):

    for i in ingr:
        if text.__contains__(i):
            return True
        
    return False


season()

