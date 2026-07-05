x = float(input("Enter the first number:- "))
y= float(input("Enter the second number:- "))
choice = input("Enter your choice (1/2/3/4): ")

if choice == '1':
    result = x + y
    print("Result:", result)

elif choice == '2':
    result = x - y
    print("Result:", result)

elif choice == '3':
    result = x * y
    print("Result:", result)

elif choice == '4':
    if y!= 0:
        result = x / y
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid choice.\nPlease select 1, 2, 3, or 4.")
