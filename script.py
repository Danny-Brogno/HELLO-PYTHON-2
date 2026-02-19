import json

# Implement a data structure to represent a recipe (e.g., dictionary, class).
class Recipe:
    
    def __init__(self, title, ingredients):
        self.title = title
        self.ingredients = ingredients
        
class CreateRecipe():
    
    def __init__(self):
        self.recipes = []

    #SAVE
    def save_recipes(self):
        
        # Convert our list of objects into a list of dictionaries
        recipe_data = []
        for r in self.recipes:
            recipe_data.append({"title": r.title, "ingredients": r.ingredients})

        # This part "writes" the file for you automatically
        with open('recipes.json', 'w') as file:
            json.dump(recipe_data, file, indent=4)
        print("Recipes saved to disk!")

    #LOAD
    def load_recipes(self):
        try:
            with open('recipes.json', 'r') as file:
                data = json.load(file) 
                self.recipes = [Recipe(item['title'], item['ingredients']) for item in data]
            print(f"Loaded {len(self.recipes)} recipes.")
        except:
            print("Starting fresh.")

    #ADD
    def add_recipe(self, title, ingredients):
        new_recipe = Recipe(title, ingredients)
        self.recipes.append(new_recipe)
        self.save_recipes()        

    #VIEW
    def view_all_recipes(self):
        if not self.recipes:
            print("Your recipe book is empty!")
        for recipe in self.recipes:
            print(f"\n--- {recipe.title.upper()} ---")
            print(f"Ingredients: {', '.join(recipe.ingredients)}")

    # SEARCH
    def search_by_title(self, title):
        search_title = lambda recipe: recipe.title.lower() == title.lower()
        return list(filter(search_title, self.recipes))

    # DELETE
    def delete_recipe(self, title):
        initial_count = len(self.recipes)
        self.recipes = [r for r in self.recipes if r.title.lower() != title.lower()]
        if len(self.recipes) < initial_count:
            print(f"Deleted '{title}'.")
            self.save_recipes()
        else:
            print("Recipe not found.")
            
    # EDIT 
    def edit_recipe(self, title, new_ingredients):
        for r in self.recipes:
            if r.title.lower() == title.lower():
                r.ingredients = new_ingredients
                self.save_recipes()
                return True
        return False

create_recipe = CreateRecipe()
create_recipe.load_recipes()

while True:
    print("\n--- RECIPE MANAGER ---")
    print("1. Add Recipe")
    print("2. View All")
    print("3. Search")
    print("4. Delete")
    print("5. Edit")
    print("6. Exit")
    
    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Title: ")
        ings = [i.strip() for i in input("Ingredients (comma separated): ").split(",")]
        create_recipe.add_recipe(title, ings)
        
    elif choice == "2":
        create_recipe.view_all_recipes()
        
    elif choice == "3":
        query = input("Enter title to search: ")
        results = create_recipe.search_by_title(query)
        if results:
            for r in results:
                print(f"Found: {r.title} - Ingredients: {r.ingredients}")
        else:
            print("No recipe found with that title.")

    elif choice == "4":
        title_to_del = input("Enter title to delete: ")
        create_recipe.delete_recipe(title_to_del)

    elif choice == "5":
        target = input("Which recipe to edit? ")
        new_ings = [i.strip() for i in input("New ingredients: ").split(",")]
        if create_recipe.edit_recipe(target, new_ings):
            print("Updated!")
        else:
            print("Not found.")

    elif choice == "6":  
        print("Goodbye!")
        break
        
#ingredients_recipe1 = ["spaghetti", "pecorino cheese", "black pepper corns", "guanciale"]
#ingredients_recipe2 = ["Stale bread", "onion", "olive oil", "pelati tomatoes", "fresh basil", "salt"]
#ingredients_recipe3 = ["Rice", "veg stock", "porcini mushrooms", "parsley", "salt", "parmiggiano reggiano cheese"]

#recipe1 = Recipe("Pasta alla Carbonara", ingredients_recipe1)
#recipe2 = Recipe("Pappa al pomodoro", ingredients_recipe2)
#recipe3 = Recipe("Risotto ai funghi", ingredients_recipe3)

#create_recipe.add_recipe(recipe1)
#create_recipe.add_recipe(recipe2)
#create_recipe.add_recipe(recipe3)

print("--- MY RECIPE BOOK ---")
create_recipe.view_all_recipes()
create_recipe.save_recipes()
