# CanadianDish


## Intro
Canadian culture is very diverse, as throughout its history it was ruled by colonized and ruled by different nations. Not only that, but the Canada was the placce where a lot of Easter-Europeans, Asians, Africans and Arabs migrated to, in order to find a better life. With such a diverse culture comes a diverse cuisine
Today it is very hard to classify what is exactly Canadian cuisine, apart of maple syrup.
This is a python program which uses API-s and Webscraping to gain access to Canadian recipes, ingredients and instructions, as well as some additional information (riddles and drinks name). It creates a ready to print PDF file with a recipe.


## Key
Featured functionalities include the followings:
-a random Canadian recipe,
-a season specific random recipe,
-a course specific random recipe,
-and one that does all of the above.


## Structure 
-CanadianDish 
-init.py 
-add.py 
-courseSeason.py 
-course.py 
-pdf.py 
-recipe.py 
-seasonal.py 
-main.py 
-demo.ipynb 
-LICENSE 
-README.md 
-setup.py


## Used API's & Sites

Sites : Recipe: https://food-guide.canada.ca/en/recipes/ , Seasonal ingredients: https://canadianfoodfocus.org/whats-in-season/

Drinks API : https://www.thecocktaildb.com/api.php, Riddle API: https://api-ninjas.com/api/riddles


## Usage


### simple.py getRecipe() - random recipe


### course.py getCourseRecipe( ??? ) - random recipe by course, 
??? - course: dinner, lunch, breakfast, snack


### seasonal.py getSeasonRecipe( ??? ) - random recipe by season,
??? - month: Full name, capitalized; default - month of today


### courseSeason getCombinedRecipe( ???, !!! ) - random recipe by course and season,
??? - course: dinner, lunch, breakfast, snack
!!! - month: Full name, capitalized; default - month of today


## License This project uses an MIT license


## Contact Name: Hrytsiv Maksym E-mail: makshrytsiv@gmail.com github: https://github.com/heliome
