def generate_multiplication_table(num):
    hundreds = num // 100
    tens = (num % 100) // 10
    units = num % 10

    for i in range(1, units + 1):
        for j in range(1, tens + 1):
            for k in range(1, hundreds + 1):

                result = i * j * k
                print(f"{i} * {j} * {k} = {result};")


number = int(input())

if number > 0:
    generate_multiplication_table(number)
