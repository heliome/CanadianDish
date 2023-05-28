from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os


def create_pdf(image_path, name, preparation_time, cooking_time, servings, ingredients, steps, tips, riddles, drinks):
    # Create the PDF document
    doc = SimpleDocTemplate("pdf.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    content = []

    # Add the image
    recipe_image = Image(image_path, width=468, height=168)
    content.append(recipe_image)

    content.append(Spacer(1, 50))

    # Add the recipe name
    recipe_name = Paragraph(f"{name}", styles["Title"])
    content.append(recipe_name)

    content.append(Spacer(1, 30))

    # Add the properties
    properties = [
        f"Preparation Time: {preparation_time}",
        f"Cooking Time: {cooking_time}",
        f"Servings: {servings}"
    ]
    recipe_properties = Paragraph("<br/>".join(properties), styles["BodyText"])
    content.append(recipe_properties)


    content.append(Spacer(1, 30))


    # Add the ingredients
    ingredient_title = Paragraph("Ingredients:", styles["Heading1"])
    content.append(ingredient_title)

    ingredient_list = ingredients.get("Ingredients", [])
    for ingredient in ingredient_list:
        ingredient_text = Paragraph(f"- {ingredient}", styles["BodyText"])
        content.append(ingredient_text)
    
    for key in ingredients.keys():

        if key != "Ingredients":
            ingredient_text = Paragraph(f"{key}", styles["BodyText"])
            content.append(ingredient_text)

            for ingredient in ingredients.get(key, []):
                ingredient_text = Paragraph(f"- {ingredient}", styles["BodyText"])
                content.append(ingredient_text)

    content.append(Spacer(1, 30))


    # Add the steps
    steps_title = Paragraph("Steps:", styles["Heading1"])
    content.append(steps_title)

    for i, step in enumerate(steps, start=1):
        step_item = Paragraph(f"Step {i}: {step}", styles["BodyText"])
        content.append(step_item)

    content.append(Spacer(1, 30))

    # Add the tips
    if len(tips) != 0:
        tips_title = Paragraph("Tips:", styles["Heading1"])
        content.append(tips_title)

        for i in tips:
            tip_item = Paragraph(f"Tip - {i}", styles["BodyText"])
            content.append(tip_item)

        content.append(Spacer(1, 30))


    #Add drinks
    drink = Paragraph(f"Would you like to drink something?", styles["Heading1"])
    content.append(drink)
    for i in drinks.keys():
        drinkType = Paragraph(f"{i} : ", styles["Heading4"])
        content.append(drinkType)
        for j in drinks[i]:
            drinkName = Paragraph(f"{j}", styles["BodyText"])
            content.append(drinkName)
        content.append(Spacer(1, 10))

    content.append(Spacer(1, 30))


    #Add riddles
    riddle = Paragraph(f"Bored while cooking? Here are some riddles :", styles["Heading1"])
    content.append(riddle)
    for i in riddles.keys():
        riddleName = Paragraph(f"{i} : ", styles["Heading4"])
        content.append(riddleName)
        riddleBody = Paragraph(f"{riddles[i][0].capitalize()}", styles["BodyText"])
        content.append(riddleBody)
        content.append(Spacer(1, 10))

    content.append(Spacer(1, 30))

    #Add riddle Answers
    riddle = Paragraph(f"Here are the answers :", styles["Heading1"])
    content.append(riddle)
    for i in riddles.keys():
        riddleName = Paragraph(f"{i} : ", styles["Heading4"])
        content.append(riddleName)
        riddleBody = Paragraph(f"{riddles[i][1].capitalize()}", styles["BodyText"])
        content.append(riddleBody)
        content.append(Spacer(1, 10))
        
    
    # Build the PDF document
    doc.build(content)
    print("PDF created!")
    os.remove(image_path)




    
