import sys

print("Which file do you want to run?")
print("1. BaseCheck")
print("2. AdvCheck")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    from operations.check_transactions import BaseCheck
elif choice == "2":
    from operations.advanced_checking import AdvCheck
else:
    print("Invalid choice")
    sys.exit(1)
