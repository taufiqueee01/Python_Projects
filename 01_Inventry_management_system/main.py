from inventory import Inventory


inventory = Inventory()

while True:
    print("\n===== Inventory Management System =====")
    print("1. Add Product")
    print("2. Update Product")
    print("3. Delete Product")
    print("4. Search Product")
    print("5. View Products")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        inventory.add_product()

    elif choice == "2":
        inventory.update_product()

    elif choice == "3":
        inventory.delete_product()

    elif choice == "4":
        inventory.search_product()

    elif choice == "5":
        inventory.view_products()

    elif choice == "6":
        print("Thank you for using Inventory Management System.")
        break

    else:
        print("Invalid choice. Please try again.")


