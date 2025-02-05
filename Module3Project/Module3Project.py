# Ice Cream Shop Application
# Date: 1/29/2025

# Store our ice cream shop's menu items
flavors = ["vanilla", "caramel", "mint", "mango", "cookies & cream", "chocolate"]
toppings = ["sprinkles", "nuts", "cherry"]
cones = ["cake cone", "sugar cone", "waffle cone"] # Adding an option to choose a cone
prices = {
    "scoop" : 2.50,
    "topping" : 0.50,
    "cone" : 1.00 # Price for adding cone
}

def display_menu():
    """Shows available flavors and toppings to the customer"""
    print("\n=== Welcome to the Ice Cream Shop! ===")
    print("\nAvailable Flavors:")

    # Loop through the flavor list and show each flavor, then
    # we'll loop through the toppings list and display them
    for flavor in flavors:
        print(f"- {flavor}")

    print("\nAvailable Toppings:")
    for topping in toppings:
        print(f"- {topping}")

    # Display the prices
    print("\nPrices:")
    print(f"Scoops: ${prices['scoop']:.2f} each")
    print(f"Toppings: ${prices['topping']:.2f} each")
    print(f"Cones: ${prices['cone']:.2f} each")

def get_flavors():
    """Gets ice cream flavor choices from the customer"""
    chosen_flavors = []

    #Use a while loop to keep taking orders until the customer is done
    while True:
        try:
            num_scoops = int(input("\nHow many scoops would you like? (1-3): "))
            if 1 <= num_scoops <= 3:
                break
            print("Please choose between 1 and 3 scoops.")
        except ValueError:
            print("Please enter a number.")
    
    # Prompt the user to enter the ice cream flavor
    print("\nFor each scoop, enter the flavor you'd like:")
    for i in range(num_scoops): # For loop prompts for each scoop of ice cream
        #Nested while loop handles the user's input and validation
        while True:
            flavor = input(f"Scoop {i+1}: ").lower()
            # Check to see if the flavor is one that's in the shop's list
            if flavor in flavors:
                chosen_flavors.append(flavor)
                break
            print("Sorry, that flavor isn't available.")

    # Return to the calling function, the number of scoops the user wants
    # and the flavors they picked
    return num_scoops, chosen_flavors

def get_toppings():
    """Gets topping choices from the customer"""
    chosen_toppings = []

    # Use a while loop to prompt the user for the toppings until they
    # are done adding toppings
    while True:
        topping = input("\nEnter a topping (or 'done' if finished): ").lower()
        # Test if the user is done ordering toppings
        if topping == 'done':
            break
        # test if the toppings is in the list of toppings for our shop
        if topping in toppings:
            chosen_toppings.append(topping)
            print(f"Added {topping}!")
        else:
            print("Sorry, that topping isn't available.")
    
    # Return the list of toppings that the user chose
    return chosen_toppings

def get_cone_choice():
    # Use a while loop to get the cone type from the customer
    while True:
        cone_choice = input("\nChoose your cone (cake cone, sugar cone or waffle cone): ").lower()
        if cone_choice in cones: 
            return cone_choice
        print("Sorry, we don't have that type of cone.")

def calculate_total(num_scoops, num_toppings, cone_choice):
    """Calculates the total cost of the order, including discounts"""
    scoop_cost = num_scoops * prices["scoop"]
    topping_cost = num_toppings * prices["topping"]
    cone_cost = prices["cone"] # Cone price doesn't change

    total =  scoop_cost + topping_cost + cone_cost

    # Adding a discount of 10% off for orders over $10
    if total > 10:
        total *= 0.90 # Apply 10% discount
        print("\nYou've received a 10% discount for orders over $10!")

    return total

def search_flavor():
    """Funtion that lets customers search for their favorite flavor"""
    search_favorite_flavor = input("\nEnter a flavor to check availability: ").lower()
    if search_favorite_flavor in flavors:
        print(f"Yes! We have {search_favorite_flavor}.")
    else:
        print(f"Sorry, we don't have {search_favorite_flavor}.")

def print_receipt(num_scoops, chosen_flavors, chosen_toppings, cone_choice):
    """Prints a nice receipt for the customer"""
    print("\n=== Your Ice Cream Order ===")
    for i in range(num_scoops):
        print(f"Scoop {i+1}: {chosen_flavors[i].title()}")
    
    print(f"\nCone: {cone_choice.title()}") 

    if chosen_toppings:
        print("\nToppings:")
        for topping in chosen_toppings:
            print(f"- {topping.title()}")
    
    #Print the total
    total = calculate_total(num_scoops, len(chosen_toppings), cone_choice)
    print(f"\nTotal: ${total:.2f}")
    
    # Save order to file
    with open("daily_orders.txt", "a") as file:
        file.write(f"\nOrder: {num_scoops} scoops, {cone_choice} - ${total:.2f}")

# Main function - Simple test function
def main():
    display_menu()
    # Call get flavors function, which returns the number of scoops
    # and the list of flavors
    num_scoops, chosen_flavors = get_flavors()
    # Call the get toppings functions which return the list of toppings
    chosen_toppings = get_toppings()
    # Call the cone choice
    cone_choice = get_cone_choice()
    # Display the receipts
    print_receipt(num_scoops, chosen_flavors, chosen_toppings, cone_choice)
    

# Automatically execute the main function when the application runs
if __name__ == "__main__":
    main()



