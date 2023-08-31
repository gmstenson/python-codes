from datetime import datetime

current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()

# day_of_week = 4

# print(day_of_week)

subtotal = float(input("\nPlease enter the subtotal: "))

tax_amount = subtotal * .06
discount = subtotal * .10

if subtotal >= 50 and day_of_week == 1 or day_of_week == 2:
    tax_amount = (subtotal - discount) * .06
    total = subtotal - discount + tax_amount

    print(f"\nDiscount amount: {discount:.2f}")
    print(f"Sales tax amount: {tax_amount:.2f}")
    print(f"Total: {total:.2f}")
    print()

else:
    total = subtotal + tax_amount

    print(f"\nSales tax amount: {tax_amount:.2f}")
    print(f"Total: {total:.2f}")
    print()

    

