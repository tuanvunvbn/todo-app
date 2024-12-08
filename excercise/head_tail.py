while True:

    with open("sides.txt", "r") as file:
        sides = file.readlines()

    user_action = input("Throw the coind and enter head or tail here: ")
    user_action = user_action.strip() + "\n"

    sides.append(user_action)

    with open("sides.txt", "w") as file:
        file.writelines(sides)

    num_heads = sides.count("head\n")
    rate_head = num_heads / len(sides) * 100

    print(f"Heads: {rate_head}%")
