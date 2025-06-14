#
#   Eric Lesende
#
#   A simple program for estimating amount of ingredients
#   needed for x amount of cookies
#

def calculate_ingredients():
    while True:
        cookies = input("Enter the number of cookies: ")

        # Ensure input is a valid number
        try:
            c = int(cookies)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        # Calculate ingredient amounts
        x = (c / 48) * 1.5
        y = (c / 48) * 1
        z = (c / 48) * 2.75

        # Display results using f-strings with 1 decimal precision
        print(f"\nYou need {x:.1f} cups of sugar, {y:.1f} cups of butter, and {z:.1f} cups of flour.")

        # Ask the user if they want to try again
        while True:
            retry = input("\nDo you want to enter another amount? (yes/no): ").strip().lower()
            if retry == "yes":
                break  # Restart loop for a new calculation
            elif retry == "no":
                print("Thanks for using the cookie calculator!")
                return  # Exit function to stop the program
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

# Run the program
calculate_ingredients()
