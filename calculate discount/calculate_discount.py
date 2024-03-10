def calculate_discount(price, discount_percent):
    #Calculate the final price after applying a discount.
    #The final price is price after applying the discount.
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
#Prompt user to enter original price and discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

#Calculate final price using calculate_discount function
final_price = calculate_discount(original_price, discount_percent)

#Print the final price after applying the discount
if final_price != original_price:
    print(f"The final price after applying a {discount_percent}% discount is: ${final_price:.2f}")
else:
    print("No discount applied. The original price remains: ${:.2f}".format(original_price))