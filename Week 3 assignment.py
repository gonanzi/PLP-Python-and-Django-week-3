def calculate_discount(price, discount_percent):
    # Check if the discount percentage is 20% or higher
    if discount_percent >= 20:
        # Calculate the discounted price
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if discount is less than 20%
        return price

# Testing for Applying a 25% discount
final_price_1 = calculate_discount(100, 25)
print(final_price_1)

# Testing for No discount applied (less than 20%)
final_price_2 = calculate_discount(100, 15)
print(final_price_2)
