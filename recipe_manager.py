import pandas as pd
import numpy as np
from ai_recipe import recommend_recipe

class RecipeManager:
    def __init__(self):
        self.recipes = {}

        try:
            df = pd.read_excel("recipes.xlsx")

            for _, row in df.iterrows():
                self.recipes[str(row["Recipe ID"])] = {
                "name": row["Recipe Name"],
                "category": row["Category"],
                "cooking_time": int(row["Cooking Time"]),
                "ingredients": row["Ingredients"].split(", "),
                "steps": row["Steps"]
            }

        except FileNotFoundError:
            pass

    def add_recipe(self):
        recipe_id = input("Enter Recipe ID: ")

        if recipe_id in self.recipes:
            print("Recipe ID already exists!")
            return

        name = input("Enter Recipe Name: ")
        category = input("Enter Category (Veg/Non-Veg): ")
        
        while True:
            try:
                cooking_time = int(input("Enter Cooking Time (in minutes): "))

                break
            except ValueError:
                print("Invalid input! Please enter a valid integer for cooking time.")


        ingredients = input(
            "Enter Ingredients (comma separated): "
        ).split(",")

        ingredients = [i.strip() for i in ingredients]

        steps = input("Enter Preparation Steps: ")

        self.recipes[recipe_id] = {
            "name": name,
            "category": category,
            "cooking_time": cooking_time,
            "ingredients": ingredients,
            "steps": steps
        }
        self.export_to_excel()
        print("Recipe Added Successfully!")

    def view_all_recipes(self):
        if not self.recipes:
            print("No recipes found.")
            return

        for recipe_id, details in self.recipes.items():
            print("\nRecipe ID:", recipe_id)
            print("Name:", details["name"])
            print("Category:", details["category"])
            print("Cooking Time:", details["cooking_time"])
            print("Ingredients:", ", ".join(details["ingredients"]))
            print("Steps:", details["steps"])

    def view_recipe_by_id(self):
        recipe_id = input("Enter Recipe ID: ")

        if recipe_id not in self.recipes:
            print("Recipe not found!")
            return

        details = self.recipes[recipe_id]

        print("\nName:", details["name"])
        print("Category:", details["category"])
        print("Cooking Time:", details["cooking_time"])
        print("Ingredients:", ", ".join(details["ingredients"]))
        print("Steps:", details["steps"])

    def update_recipe(self):
        recipe_id = input("Enter Recipe ID: ")

        if recipe_id not in self.recipes:
            print("Recipe not found!")
            return

        ingredients = input(
            "Enter New Ingredients: "
        ).split(",")

        ingredients = [i.strip() for i in ingredients]

        steps = input("Enter New Steps: ")

        self.recipes[recipe_id]["ingredients"] = ingredients
        self.recipes[recipe_id]["steps"] = steps
        self.export_to_excel()
        print("Recipe Updated Successfully!")

    def delete_recipe(self):
        recipe_id = input("Enter Recipe ID: ")

        if recipe_id not in self.recipes:
            print("Recipe not found!")
            return

        del self.recipes[recipe_id]
        self.export_to_excel()
        print("Recipe Deleted Successfully!")

    def export_to_excel(self):
        data = []

        for recipe_id, details in self.recipes.items():
            data.append({
                "Recipe ID": recipe_id,
                "Recipe Name": details["name"],
                "Category": details["category"],
                "Cooking Time": details["cooking_time"],
                "Ingredients": ", ".join(details["ingredients"]),
                "Steps": details["steps"]
            })

        df = pd.DataFrame(data)
        df.to_excel("recipes.xlsx", index=False)

        print("Data Exported Successfully to recipes.xlsx!")

    def most_used_ingredient(self):
        ingredients = []

        for details in self.recipes.values():
            ingredients.extend(details["ingredients"])

        if not ingredients:
            print("No ingredients found.")
            return

        arr = np.array(ingredients)

        unique, counts = np.unique(arr, return_counts=True)

        max_index = np.argmax(counts)

        print("Most Used Ingredient:",
              unique[max_index])

    def ai_recipe_assistant(self):
        ingredients = input("Enter Available Ingredients: ")

        result = recommend_recipe(ingredients)

        print("\nGroq Suggests:\n")
        print(result)

    def menu(self):
        while True:
            print("\n===== RECIPE MANAGER =====")
            print("1. Add Recipe")
            print("2. View All Recipes")
            print("3. View Recipe By ID")
            print("4. Update Recipe")
            print("5. Delete Recipe")
            print("6. Most Used Ingredient")
            print("7. AI Recipe Assistant")
            print("8. Exit")

            choice = input("Enter Choice(1/2/3/4/5/6/7/8): ")

            if choice == "1":
                self.add_recipe()

            elif choice == "2":
                self.view_all_recipes()

            elif choice == "3":
                self.view_recipe_by_id()

            elif choice == "4":
                self.update_recipe()

            elif choice == "5":
                self.delete_recipe()

            elif choice == "6":
                self.most_used_ingredient()

            elif choice == "7":
                self.ai_recipe_assistant()

            elif choice == "8":
                print("Recipes Saved Successfully!")
                print("Thank You!")
                break
manager = RecipeManager()
manager.menu()
