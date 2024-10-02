def cat_diet(fat, proteins, carbohydrates, total_calories, water_perc):
    total_fat = total_calories * (fat / 100) / 9
    total_proteins = total_calories * (proteins / 100) / 4
    total_carbohydrates = total_calories * (carbohydrates / 100) / 4

    food_cilos = total_fat + total_proteins + total_carbohydrates
    gram_of_food = total_calories / food_cilos
    total_percent = 100 - water_perc
    calories = gram_of_food * (total_percent / 100)

    return calories


fat = int(input())
proteins = int(input())
carbohydrates = int(input())
total_calories = int(input())
water_perc = int(input())
result = cat_diet(fat, proteins, carbohydrates, total_calories, water_perc)
print(f"{result:.4f}")