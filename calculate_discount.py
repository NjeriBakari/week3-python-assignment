# Python Discount Calculator Assignment
# Function to calculate discount and user interaction

def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Parameters:
    price (float): The original price of the item
    discount_percent (float): The discount percentage to apply
    
    Returns:
    float: The final price after discount (if 20% or higher) or original price
    """
    # Check if discount is 20% or higher
    if discount_percent >= 20:
        # Calculate discount amount
        discount_amount = price * (discount_percent / 100)
        # Calculate final price after discount
        final_price = price - discount_amount
        return final_price
    else:
        # Return original price if discount is less than 20%
        return price

# Main program execution
def main():
    print("=" * 50)
    print("         DISCOUNT CALCULATOR")
    print("=" * 50)
    print("Note: Discount is only applied if it's 20% or higher")
    print("-" * 50)
    
    try:
        # Prompt user for original price
        original_price = float(input("Enter the original price of the item: $"))
        
        # Validate price input
        if original_price < 0:
            print("Error: Price cannot be negative!")
            return
        
        # Prompt user for discount percentage
        discount_percentage = float(input("Enter the discount percentage: "))
        
        # Validate discount percentage
        if discount_percentage < 0:
            print("Error: Discount percentage cannot be negative!")
            return
        
        # Calculate final price using the function
        final_price = calculate_discount(original_price, discount_percentage)
        
        # Display results
        print("\n" + "=" * 50)
        print("CALCULATION RESULTS")
        print("=" * 50)
        print(f"Original Price: ${original_price:.2f}")
        print(f"Discount Percentage: {discount_percentage}%")
        
        if discount_percentage >= 20:
            discount_amount = original_price - final_price
            savings = discount_amount
            print(f"Discount Applied: YES (≥20%)")
            print(f"Discount Amount: ${discount_amount:.2f}")
            print(f"Final Price: ${final_price:.2f}")
            print(f"You saved: ${savings:.2f}")
        else:
            print(f"Discount Applied: NO (<20%)")
            print(f"Final Price: ${final_price:.2f}")
            print("No discount applied - minimum 20% required")
        
        print("=" * 50)
        
    except ValueError:
        print("Error: Please enter valid numeric values!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Test function with predefined values
def test_function():
    print("\n" + "=" * 50)
    print("TESTING THE FUNCTION WITH SAMPLE VALUES")
    print("=" * 50)
    
    test_cases = [
        (100, 25),    # Should apply discount
        (50, 15),     # Should not apply discount
        (200, 30),    # Should apply discount
        (75, 20),     # Should apply discount (exactly 20%)
        (120, 5)      # Should not apply discount
    ]
    
    for price, discount in test_cases:
        result = calculate_discount(price, discount)
        status = "Applied" if discount >= 20 else "Not Applied"
        print(f"Price: ${price}, Discount: {discount}% → Final: ${result:.2f} ({status})")

if __name__ == "__main__":
    # Run the main program
    main()
    
    # Ask if user wants to see test examples
    print("\n" + "-" * 50)
    show_tests = input("Would you like to see test examples? (y/n): ").lower()
    if show_tests in ['y', 'yes']:
        test_function()
    
    print("\nThank you for using the Discount Calculator!")

# Additional utility functions for enhanced functionality
def calculate_multiple_discounts():
    """Allow user to calculate multiple discounts in one session"""
    print("\n" + "=" * 50)
    print("MULTIPLE DISCOUNT CALCULATIONS")
    print("=" * 50)
    
    while True:
        try:
            price = float(input("\nEnter price (or 0 to exit): $"))
            if price == 0:
                break
                
            discount = float(input("Enter discount percentage: "))
            final = calculate_discount(price, discount)
            
            print(f"Result: ${price:.2f} → ${final:.2f}")
            
        except ValueError:
            print("Please enter valid numbers!")
        except KeyboardInterrupt:
            break
    
    print("Session ended.")

# Uncomment the line below to enable multiple calculations feature
# calculate_multiple_discounts()