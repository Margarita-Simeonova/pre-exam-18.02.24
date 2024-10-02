def bracelet_stand(poket_money, seal_money, expenses, present_price):
    total_poket_money = 5 * poket_money
    total_seal_money = 5 * seal_money
    total_money = (total_poket_money + total_seal_money) - expenses

    if total_money >= present_price:
        return f"Profit: {total_money:.2f} BGN, the gift has been purchased."
    else:
        return f"Insufficient money: {present_price - total_money:.2f} BGN."


poket_money = float(input())
seal_money = float(input())
expenses = float(input())
present_price = float(input())
result = bracelet_stand(poket_money, seal_money, expenses, present_price)
print(result)
