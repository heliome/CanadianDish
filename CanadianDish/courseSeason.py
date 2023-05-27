from datetime import datetime
import ingredients
import recipe

def courseSeason():
    
    course = input()
    if course.lower() == "dinner" or course.lower() == "lunch":
        n = "f%5B0%5D=meal%3A46&" 
    elif course.lower() == "breakfast":
        n = "f%5B0%5D=meal%3A45&"
    elif course.lower() == "snack":
        n = "f%5B0%5D=meal%3A47&"
    else:
        return("check the name of the course")
    
    month = datetime.now().strftime('%B')

    ingr = ingredients.ingredient(month)

    text = recipe.rand(n)
    while check(ingr, text):
        text = recipe.rand(n)
    print(text)
    

def check(ingr, text):

    for i in ingr:
        if text.__contains__(i):
            return True
        
    return False
courseSeason()

