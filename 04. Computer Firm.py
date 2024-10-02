def computer_firm(computers_count):
    total_sales = 0
    total_rating = 0
    for comp in range(computers_count):
        number = int(input())
        rating = number % 10
        sales = number // 10

        if rating == 2:
            total_sales += 0
        elif rating == 3:
            total_sales += sales / 2
        elif rating == 4:
            total_sales += sales * 0.7
        elif rating == 5:
            total_sales += sales * 0.85
        elif rating == 6:
            total_sales += sales

        total_rating += rating

    average_rating = total_rating / computers_count
    return f"{total_sales:.2f}\n{average_rating:.2f}"


computers_count = int(input())
result = computer_firm(computers_count)
print(result)
