# Implement a data structure to represent a recipe (e.g., dictionary, class).
class Recipe:
    
    def __init__(self, title, ingredients):
        self.title = title
        self.ingredients = ingredients
        
class CreateRecipe():
    
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe_object):
        self.recipes.append(recipe_object)
        print(f"Added: {recipe_object.title}")
        
    def view_all_recipes(self):
        for recipe in self.recipes:
            print(f"\n--- {recipe.title.upper()} ---")
            print(f"Ingredients: {', '.join(recipe.ingredients)}")

    # Search for books by title 
    def search_by_title(self, title):
        search_title = lambda recipe: recipe.title.lower() == title.lower()
        return list(filter(search_title, self.recipes))

create_recipe = CreateRecipe()

ingredients_recipe1 = ["spaghetti", "pecorino cheese", "black pepper corns", "guanciale"]
ingredients_recipe2 = ["Stale bread", "onion", "olive oil", "pelati tomatoes", "fresh basil", "salt"]
ingredients_recipe3 = ["Rice", "veg stock", "porcini mushrooms", "parsley", "salt", "parmiggiano reggiano cheese"]

recipe1 = Recipe("Pasta alla Carbonara", ingredients_recipe1)
recipe2 = Recipe("Pappa al pomodoro", ingredients_recipe2)
recipe3 = Recipe("Risotto ai funghi", ingredients_recipe3)

create_recipe.add_recipe(recipe1)
create_recipe.add_recipe(recipe2)
create_recipe.add_recipe(recipe3)

print("--- MY RECIPE BOOK ---")
create_recipe.view_all_recipes()
