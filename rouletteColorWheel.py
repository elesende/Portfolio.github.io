#
#    Eric Lesende
#
#    rouletteColorWheel.py
#
#    Roulette Wheel Colors App
#    Determines the color of a roulette wheel pocket based on user input (0–36)
#

def main():
    # Introduction
    print('\nRoulette Wheel Colors App ...\n')

    # Main program loop
    while True:
        # Input validation loop: ensures input is an integer within 0–36
        while True:
            try:
                number = int(input('Please enter pocket number (0-36): '))
                if 0 <= number <= 36:
                    break  # Valid input, exit loop
                else:
                    print('Invalid input. Number is not in the correct range (0-36). Please try again.\n')
            except ValueError:
                print('Invalid input. Please enter a valid integer.\n')

        # Determine and display color based on roulette rules
        if number == 0:
            print('The Color of the Wheel Pocket is Green')
        elif 1 <= number <= 10:
            print('The Color of the Wheel Pocket is Red' if number % 2 != 0 else 'The Color of the Wheel Pocket is Black')
        elif 11 <= number <= 18:
            print('The Color of the Wheel Pocket is Black' if number % 2 != 0 else 'The Color of the Wheel Pocket is Red')
        elif 19 <= number <= 28:
            print('The Color of the Wheel Pocket is Red' if number % 2 != 0 else 'The Color of the Wheel Pocket is Black')
        elif 29 <= number <= 36:
            print('The Color of the Wheel Pocket is Black' if number % 2 != 0 else 'The Color of the Wheel Pocket is Red')

        # Ask the user if they want to run the program again
        while True:
            retry = input('Would you like to try again? (yes or no): ').strip().lower()
            if retry == 'yes':
                print()  # Adds a blank line for readability before restarting
                break     # Breaks inner loop to restart from the top
            elif retry == 'no':
                print('\nThank you for using the Roulette Wheel Colors App!')
                return     # Exits the program
            else:
                print('Invalid input. Please enter either "yes" or "no".\n')

# Call the main function to start the program
main()
