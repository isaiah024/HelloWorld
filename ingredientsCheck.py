cookbook = {"spaghetti": {"tomatoes", "pasta", "cheese"},
            "lasagna": {"pasta", "tomatoes", "cheese"}
            }

def checkIngredients(currIng):
    for x in cookbook:
        if currIng == cookbook[x]:
            print("You could make: " + x)

def addRecipe(recipeName, recipeList):
    newDict = {recipeName: recipeList}
    cookbook.update(newDict)

def printRecipes():
    print(cookbook)

if __name__ == '__main__':
    ing = {"tomatoes", "pasta", "cheese"}
    addRecipe("tacos", {"beef", "tortillas"})
    checkIngredients(ing)
    printRecipes()
