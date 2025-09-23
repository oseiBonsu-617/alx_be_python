def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def user_item():
    return 

def main():
    shopping_list = []

    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter an item to be added to the shopping list: ")
            shopping_list.append(item)

        elif choice == '2':
            # Prompt for and remove an item
            item = int(input("Enter an item number to be removed from the shopping list: "))
            del shopping_list[item + 1]

        elif choice == '3':
            # Display the shopping list
            print('******SHOPPING LIST******')
            for index, list in enumerate(shopping_list):
                print(f'{index + 1}. {list}')
            
        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
            