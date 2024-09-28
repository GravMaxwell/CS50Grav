# was working on my cs50 hw while at work plz don't tell my boss :)

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total_cost = 0.0

while True:
    try:
        item = input("Item: ").title()
        if item in menu:
            # from problem hint: d[key] ... if key in d ..
            total_cost += menu[item]
            print(f"Total: ${total_cost:.2f}")
        else:
            print("Item not found. Please try again.")
    # catch when user hits "ctrl+d"
    except EOFError:
        print("\n")
        break
