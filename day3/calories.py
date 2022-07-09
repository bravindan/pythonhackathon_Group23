

number_of_fat_grams = int(input("How many grams of fat did you consume? "))
number_of_carb_grams = int(input("How many grams of carbohydrates did you consume? "))
calories_from_fat = number_of_fat_grams * 9
calories_from_carb = number_of_carb_grams * 4
total_calories = calories_from_fat + calories_from_carb
print("Calories from fat:", calories_from_fat)
print("Calories from carbs:", calories_from_carb)
print("You consumed", total_calories, "calories")
