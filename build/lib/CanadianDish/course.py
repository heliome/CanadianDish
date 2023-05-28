import recipe
import pdf
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

        #Get all the data and create pfd of it
        img, name, preparation, cooking, serves, ingredients, steps, tips = recipe.rand(z)
        riddles, drinks = adds.add()
        pdf.create_pdf(img, name, preparation, cooking, serves, ingredients, steps, tips, riddles, drinks)
    
    except:
        print("Sorry, we have a problem, please try again later")

getRecipe()