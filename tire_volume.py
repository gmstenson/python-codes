"""
File: tire_volume.py
Author: Gizelle Stenson

W02 Prove: Calling Functions
"""

# import math library and datetime class to be used in this program 
# for computation and getting the current date from computer's OS
import math 
from datetime import datetime

# opens the file and appends input data to the end of the file
with open("volumes.txt", "at") as tire_volumes:

    # function to return volume of space inside a tire
    def volume(width, aspect_ratio, diameter):
        return (math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

    # gets current date from computer and post in a format
    date = datetime.now()
    current_date = date.strftime("%Y-%m-%d %H:%M:%S")

    # user inputs data
    # used 'float' instead of 'int' for decimal numbers
    width = float(input("\nEnter the width of the tire in mm (ex 205): "))
    aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

    volume_of_space = volume(width, aspect_ratio, diameter)

    # tire prices based on tireplus.com 
    tire_price_300_50_15 = 415.99
    tire_price_300_20_15 = 306.99
    tire_price_200_60_15 = 150.99
    tire_price_200_30_15 = 179.99
    other_tire_price = 129.99

    print(f"\nThe approximate volume is {volume_of_space:.2f} liters")

    # STRETCH CHALLENGE #1 - if-elif-else statements to find the right price based on input data
    if width >= 300 and aspect_ratio >= 50 and diameter >= 15:
        print(f"The price of the tire is ${tire_price_300_50_15}")

        # STRETCH CHALLENGE #2 - ask user if he wants to buy the tire 
        ask_to_buy = input("\nDo you want to buy the tire? (yes/no) --> ")

        # if yes, program asks for phone number then stores the phone number in the file
        if ask_to_buy.lower() == "yes" or ask_to_buy.lower() == "y":
            phone_number = input("\nPlease enter phone number: ")
            print("Thank you!")

            # all input data including current date, volume of space, tire price, and phone number stores in the file
            print(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume_of_space:.2f}, ${tire_price_300_50_15}, {phone_number}", file=tire_volumes)
        
        else:
            print("Thank you!")
            print(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume_of_space:.2f}, ${tire_price_300_50_15}", file=tire_volumes)

    elif width >= 300 and aspect_ratio >= 20 and diameter >= 15:
        print(f"The price of the tire is ${tire_price_300_20_15}")
        ask_to_buy = input("\nDo you want to buy the tire? (yes/no) --> ")

        if ask_to_buy.lower() == "yes" or ask_to_buy.lower() == "y":
            phone_number = input("\nPlease enter phone number: ")
            print("Thank you!")
            print(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume_of_space:.2f}, ${tire_price_300_20_15}, {phone_number}", file=tire_volumes)
    
        else:
            print("Thank you!")
            print(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume_of_space:.2f}, ${tire_price_300_20_15}", file=tire_volumes)

    elif width >= 200 and aspect_ratio >= 60 and diameter >= 15:
        print(f"The price of the tire is ${tire_price_200_60_15}")
        ask_to_buy = input("\nDo you want to buy the tire? (yes/no) --> ")

        if ask_to_buy.lower() == "yes" or ask_to_buy.lower() == "y":
            phone_number = input("\nPlease enter phone number: ")
            print("Thank you!")
            print(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume_of_space:.2f}, ${tire_price_200_60_15}, {phone_number}", file=tire_volumes)

        else:
            print("Thank you!")
            print(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume_of_space:.2f}, ${tire_price_200_60_15}", file=tire_volumes)

    elif width >= 200 and aspect_ratio >= 30 and diameter >= 15:
        print(f"The price of the tire is ${tire_price_200_30_15}")
        ask_to_buy = input("\nDo you want to buy the tire? (yes/no) --> ")

        if ask_to_buy.lower() == "yes" or ask_to_buy.lower() == "y":
            phone_number = input("\nPlease enter phone number: ")
            print("Thank you!")
            print(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume_of_space:.2f}, ${tire_price_200_30_15}, {phone_number}", file=tire_volumes)

        else:
            print("Thank you!")
            print(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume_of_space:.2f}, ${tire_price_200_30_15}", file=tire_volumes)

    else:
        print(f"The price of the tire is ${other_tire_price}")
        ask_to_buy = input("\nDo you want to buy the tire? (yes/no) --> ")

        if ask_to_buy.lower() == "yes" or ask_to_buy.lower() == "y":
            phone_number = input("\nPlease enter phone number: ")
            print("Thank you!")
            print(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume_of_space:.2f}, ${other_tire_price}, {phone_number}", file=tire_volumes)

        else:
            print("Thank you!")
            print(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume_of_space:.2f}, ${other_tire_price}", file=tire_volumes)


    print()
