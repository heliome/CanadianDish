from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(image_path, name, preparation_time, cooking_time, servings, ingredients, steps, tips):
    # Create the PDF document
    doc = SimpleDocTemplate("pdf.pdf", pagesize=letter)

    # Set up the styles
    styles = getSampleStyleSheet()

    # Define the content for the PDF
    content = []

    # Add the image
    recipe_image = Image(image_path, width=468, height=168)
    content.append(recipe_image)

    # Add spacing between image and name
    content.append(Spacer(1, 50))

    # Add the recipe name
    recipe_name = Paragraph(f"{name}", styles["Title"])
    content.append(recipe_name)

    # Add spacing between name and servings
    content.append(Spacer(1, 20))

    # Add the properties
    properties = [
        f"Preparation Time: {preparation_time}",
        f"Cooking Time: {cooking_time}",
        f"Servings: {servings}"
    ]
    recipe_properties = Paragraph("<br/>".join(properties), styles["BodyText"])
    content.append(recipe_properties)

    # Add spacing between servings and ingredients
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

    # Add spacing between ingredients and steps
    content.append(Spacer(1, 30))

    # Add the steps
    steps_title = Paragraph("Steps:", styles["Heading1"])
    content.append(steps_title)

    for index, step in enumerate(steps, start=1):
        step_text = Paragraph(f"Step {index}: {step}", styles["BodyText"])
        content.append(step_text)

    # Add spacing between steps and tips
    content.append(Spacer(1, 30))

    # Add the tips
    tips_title = Paragraph("Tips:", styles["Heading1"])
    content.append(tips_title)

    for index, tip in enumerate(tips, start=1):
        tip_text = Paragraph(f"Tip {index}: {tip}", styles["BodyText"])
        content.append(tip_text)

    # Build the PDF document
    doc.build(content)

