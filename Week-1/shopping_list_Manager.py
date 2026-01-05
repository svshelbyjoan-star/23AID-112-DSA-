L = []
ans = input("do you want to do anything with your shopping list? (y/n): ")
while ans == 'y':
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4.quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        item = input("Enter the item to add: ")
        L.append(item)
        print(item + " has been added to the list.")
    elif choice == 2:
        item = input("Enter the item to remove: ")
        if item in L:
            L.remove(item)
            print(item + " has been removed from the list.")
        else:
            print(item + " is not in the list.")
    elif choice == 3:
        print("Your shopping list:")
        for i in L:
            print("- " + i)
    else:
        break