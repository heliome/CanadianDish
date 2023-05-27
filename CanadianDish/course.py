import recipe

def getRecipe():
    course = input()
    if course.lower() == "dinner" or course.lower() == "lunch":
        n = "?f%5B0%5D=meal%3A46" 
    elif course.lower() == "breakfast":
        n = "?f%5B0%5D=meal%3A45"
    elif course.lower() == "snack":
        n = "?f%5B0%5D=meal%3A47"
    else:
        return("check the name of the course")


    text = recipe.rand(n)
    print(text)

getRecipe()