def excursion_sale(sea_count, mountain_count):
    total_money = 0
    sea = sea_count
    mountain = mountain_count

    while not sea == 0 or not mountain == 0:
        data = input()
        if data == "Stop":
            break
        if data == "sea":
            if sea == 0:
                continue
            total_money += 680
            sea -= 1

        elif data == "mountain":
            if mountain == 0:
                continue
            total_money += 499
            mountain -= 1

    if sea == 0 and mountain == 0:
        return f"Good job! Everything is sold.\nProfit: {int(total_money)} leva."
    else:
        return f"Profit: {int(total_money)} leva."


sea_count = int(input())
mountain_count = int(input())
result = excursion_sale(sea_count, mountain_count)
print(result)