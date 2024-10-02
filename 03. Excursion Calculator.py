def excursion_calculator(people_count, season):
    price = 0
    if season == "spring":
        if people_count <= 5:
            price = people_count * 50
        else:
            price = people_count * 48
    elif season == "summer":
        if people_count <= 5:
            price = people_count * 48.5
        else:
            price = people_count * 45
        price *= 0.85
    elif season == "autumn":
        if people_count <= 5:
            price = people_count * 60
        else:
            price = people_count * 49.5
    elif season == "winter":
        if people_count <= 5:
            price = people_count * 86
        else:
            price = people_count * 85
        price *= 1.08

    return f"{price:.2f} leva."


people_count = int(input())
season = input()
result = excursion_calculator(people_count, season)
print(result)