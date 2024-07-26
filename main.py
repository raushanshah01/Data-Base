import sys

while True:
    sys.stdout.write("\nStudent Menu:\n")
    sys.stdout.write("1. Add a Student\n")
    sys.stdout.write("2. Search Student\n")
    sys.stdout.write("3. Delete details\n")
    sys.stdout.write("4. Modify sudent data.\n")
    sys.stdout.write("5. Exit\n")
    choice = input("Enter your choice: ")
    if choice == '1':
        import addstudent
        addstudent.student()
    elif choice == '2':
        import search
        search.search()
    elif choice == '3':
        import delete
        delete.delete()
    elif choice== '4':
        import modify
        modify.modify_data()
    elif choice == '5':
        sys.stdout.write("Exiting...")
        break
    else:
        sys.stdout.write("Invalid choice. Please choose again.")
