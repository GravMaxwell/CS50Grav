def main():
    # make an empty dictionary to store the grocery items and item count
    grocery_list = {}
    print("" , end='')
    try:
        while True:
            # read user's input, remove any whitespace and make lowercase
            item = input().strip().lower()

            # check if item is in the dictionary
            if item in grocery_list:
                # increment by 1 if item is in dict
                grocery_list[item] += 1

            else:
                # if item is not in dictionary, add item to dictionary with qty 1
                grocery_list[item] = 1
    except EOFError:
        # end prompt when user hits ctrl-d
        pass
    # sort items (keys) in dictionary alphabetically
    cart = sorted(grocery_list.keys())

    # print each item and count and format output in ALL CAPS
    for item in cart:
        print(f"{grocery_list[item]} {item.upper()}")

main()
