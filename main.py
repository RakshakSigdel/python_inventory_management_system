"""
WeCare Inventory Management System - Main Module

This module serves as the entry point for the weCare Inventory Management System.
It provides a command-line interface for users to interact with the system,
offering options to display inventory, sell items, restock inventory, and exit.

Author: [Rakshak Sigdel]
Version: 1.0
"""

from operation import sell_item, display_menu,display_all_products,buy_items,display_menu

def main():
    """
    Main function that drives the inventory management system.
    
    This function displays a menu of operations and processes user input
    to perform various inventory management tasks including:
    - Displaying current inventory
    - Selling items
    - Restocking inventory
    - Exiting the program
    
    The function handles user input validation and provides appropriate feedback.
    
    Returns:
        None
    """
    
    # Call the display menu function to show options
    display_menu()

    # Main program loop
    end_program = False
    while not end_program:
        try:
            # Get user choice from menu options
            user_input = input("Please enter your choice(1,2,3,4): ")
            
            # Process user choice
            if user_input == '1':
                print("🖥️You choose to display items.")
                display_all_products()
                input("🏠Press Enter to return to main menu...")
                display_menu()
            elif user_input == '2':
                print("💲You choose to sell items.")
                sell_item()
                input("🏠Press Enter to return to main menu...")
                display_menu()
            elif user_input == '3':
                print("➕You choose to add items.")
                buy_items()
                input("🏠Press Enter to return to main menu...")
                display_menu()
            elif user_input == '4':
                print("👋You choose to exit the program.")
                print("Thank you for using WeCare!")
                end_program = True
            else:
                print("Invalid input. Please enter 1, 2, 3, or 4.")
        except ValueError:
            print("Invalid input. Please enter only a number (1, 2, 3, or 4) without any other characters.")
           
# Execute the main function
main()