def main():
    # create a dictionary of fruits and their calorie counts
    fruits = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80,
        }

    # prompt the user for an item
    item = input("Item: ").strip().lower()

    # check if the item is in the dictionary and print the calories
    if item in fruits:
        print(f"Calories: {fruits[item]}")

main()
