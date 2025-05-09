"""
WeCare Inventory Management System - Operations Module

This module handles the core operations for the WeCare Inventory Management System.
It provides comprehensive functionality for:
1. User Interface: Displaying the main menu and product listings
2. Sales Management: Processing customer purchases with the "Buy 3 Get 1 Free" promotion
3. Inventory Management: Restocking existing items and adding new products
4. Documentation: Generating detailed invoices for both sales and purchases

The module maintains accurate inventory records across all transactions and
provides a user-friendly interface for staff to manage the complete
inventory lifecycle.

Author: [Rakshak Sigdel]
Version: 1.0
"""

from read import read_from_file
from write import buy_items_invoice,sell_item_invoice,save_to_inventory

def display_menu():
    """
    Displays the Options available in the management system.
    
    Returns:
        None
    """
    print("""
          ╔════════════════════════════════════════╗
          ║                                        ║ 
╔═════════╚════════════════════════════════════════╝═════════╗
║                  🌟 Welcome to weCare 🌟                   ║
║               Your Inventory Management System             ║
╠════════════════════════════════════════════════════════════╣
║<~•~•~•~•~•~•~•~•~•~ Management Options ~•~•~•~•~•~•~•~•~•~>║
║▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓║
║                1️  ✨ SHOW ME THE GOODS ✨                 ║
║                2️  💸 SELL STUFF 💸                        ║
║                3️  🔄 RESTOCK THE SHELVES 🔄               ║
║                4️  👋 PEACE OUT 👋                         ║
╚════════════════════════════════════════════════════════════╝
""")

def display_all_products():
    """
    Displays the current inventory in a formatted table.
    
    This function processes inventory data and displays it in a well-formatted
    table showing product ID, name, brand, quantity, cost, and origin.
    The cost shown is doubled from the stored value (representing retail price).
    
    Parameters:
        None
        
    Returns:
        None
    """
    # Get inventory data from file
    data = read_from_file()
    
    # Print table header
    print("╔" + "═" * 79 + "╗")
    print("║" + "                                  Product List                                 " + "║")
    print("╠" + "═" * 79 + "╣")
    print("║ID ║       Name         ║    Brand     ║   Qty    ║  Cost    ║     Origin      ║")
    print("╠" + "═" * 79 + "╣")

    for key in data:
        id_val, name, brand, qty, cost, origin = data[key]
        
        id_space = " "
        id_display = id_space + id_val + id_space if (len(id_val) <= 4) else id_space + id_val[:3] + ".. "
        
        if len(name) > 18:
            name_display = name[:16] + ".."
        else:
            name_display = name + " " * (18 - len(name))
        
        if len(brand) > 12:
            brand_display = brand[:10] + ".."
        else:
            brand_display = brand + " " * (12 - len(brand))
        
        qty_str = str(qty)
        if len(qty_str) > 8:
            qty_display = qty_str[:6] + ".."
        else:
            qty_display = qty_str + " " * (8 - len(qty_str))
        
        cost_doubled = str(float(cost) * 2)
        if len(cost_doubled) > 8:
            cost_display = cost_doubled[:6] + ".."
        else:
            cost_display = cost_doubled + " " * (8 - len(cost_doubled))
        
        if len(origin) > 15:
            origin_display = origin[:13] + ".."
        else:
            origin_display = origin + " " * (15 - len(origin))
        
        print(
            "║" + id_display + 
            "║ " + name_display + 
            " ║ " + brand_display + 
            " ║ " + qty_display + 
            " ║ " + cost_display + 
            " ║ " + origin_display + " ║"
        )
    # Print table footer
    print("╚" + "═" * 79 + "╝")
    
def sell_item():
    """
    Manages the process of selling items to customers.
    
    This function provides a comprehensive user interface to:
    - Display the current inventory to the sales staff
    - Process sales transactions for multiple customers
    - Implement a "Buy 3 Get 1 Free" promotion
    - Validate user inputs to ensure data integrity
    - Update inventory levels after successful sales
    - Generate professional sales invoices for customers
    
    The function maintains accurate inventory records by updating
    the data file after each transaction and provides detailed
    feedback throughout the sales process.
    
    Parameters:
        None
        
    Returns:
        None
    """
    while True:  # Outer loop for multiple customers
        print("""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                        🛒 SALES MANAGEMENT 🛒                                 ║
╚═══════════════════════════════════════════════════════════════════════════════╝
""")
        display_all_products()
        
        #Storing the product data in a dictionary
        data = read_from_file()
        
        print("\n" + "─" * 50)
        print("👤 CUSTOMER INFORMATION")
        print("─" * 50)
        customer_name = input("📝 Customer Name: ")
        print("─" * 50)
        
        #creating a list to store the items for invoice
        items_for_invoice = []
        
        keep_selling = True  #Inner loop for selling items to the same customer
        while keep_selling:
            try:
                print("\n" + "═" * 60)
                print("🔍 PRODUCT SELECTION")
                print("═" * 60)
                
                #Getting product ID with validation
                while True:
                    try:
                        product_id = int(input("🔢 Enter Product ID: "))
                        if product_id in data:
                            break
                        else:
                            print("⚠️ Invalid product ID. Please try again.")
                    except ValueError:
                        print("⚠️ Invalid input. Please enter a number.")
                
                available_quantity = int(data[product_id][3]) 
                quantity_for_sale = available_quantity - (available_quantity // 4) #To maintain the buy 3 get 1 free policy
                # Display selected product information
                print("\n" + "─" * 60)
                print("🏷️ SELECTED: Item #" + str(product_id) + " - " + data[product_id][0])
                print("─" * 60)
                print("• Brand: " + data[product_id][1])
                print("• Quantity in stock: " + str(data[product_id][3]))
                print("• Available for sale: " + str(quantity_for_sale))
                print("• Unit Price: $" + str(round(float(data[product_id][4]), 2)))
                print("• Origin: " + data[product_id][5])
                print("─" * 60)

                while True:
                    try:
                        quantity = int(input("📦 Enter Quantity to Purchase: "))
                        if quantity > quantity_for_sale:
                            print("⚠️ Insufficient stock. We can only sell "+ str(quantity_for_sale) +" items to maintain buy three get one free policy")
                        elif quantity <= 0:
                            print("⚠️ Invalid quantity. Please enter a positive number.")
                        else:
                            break
                    except ValueError:
                        print("⚠️ Invalid input. Please enter a number.")
                
                free_product = quantity // 3
                unit_cost = float(data[product_id][4])
                total_cost = quantity * unit_cost
                
                # Show transaction summary
                print("\n" + "─" * 60)
                print("🧮 TRANSACTION SUMMARY")
                print("─" * 60)
                print("• Item: " + data[product_id][0])
                print("• Quantity: " + str(quantity))
                print("• Free Items (Buy 3 Get 1): " + str(free_product))
                print("• Price Per Unit: $" + str(round(float(data[product_id][3]), 2)))
                print("• Subtotal: $" + str(round(total_cost, 2)))
                print("─" * 60)

                
                #update quantity
                data[product_id][3] = str(available_quantity - quantity - free_product)
                #update the item_for_invoice
                items_for_invoice.append([
                    product_id,
                    data[product_id][1],
                    quantity,
                    free_product,
                    total_cost,
                    unit_cost
                ])
                #update the data file
                save_to_inventory(data)
                        
                # Ask to continue with current customer
                print("\n" + "─" * 60)
                print("🔄 CONTINUE WITH CURRENT CUSTOMER?")
                print("─" * 60)
                user_input = input("Want to sell more items to " + customer_name + "? (Y/N): ")
                if user_input.lower() != "y":
                    keep_selling = False
            except Exception as e:
                print("❌ An unexpected error occurred: "+   str(e))
                print("⚠️ No items available for sale.")
                break 
               
        if items_for_invoice:
            print("\n" + "═" * 60)
            print("📊 FINALIZING TRANSACTION")
            print("═" * 60)
            
            try:
                print("\n" + "─" * 60)
                print("🧾 GENERATING INVOICE")
                print("─" * 60)
                print("Customer: " +  customer_name)
                print("Items Processed: " + str(len(items_for_invoice)))
                
                # Generate the invoice
                sell_item_invoice(customer_name, items_for_invoice)
                print("✅ Invoice generated successfully")
                
                # Ask if want to sell to another customer
                print("\n" + "─" * 60)
                print("👥 CONTINUE WITH NEW CUSTOMER?")
                print("─" * 60)
                new_customer = input("Want to sell to another customer? (Y/N): ")
                if new_customer != "y" and new_customer != "Y":
                    print("\n" + "─" * 60)
                    return
                # If "yes", the loop will continue and start again
                
            except IOError as e:
                print("❌ Error writing data: " +   str(e))
                return
            except Exception as e:
                print("❌ An unexpected error occurred: "+  str(e))
                return
        else:
            print("⚠️ No items were sold.")
            return

def buy_items():
    """
    Manages the process of adding new items or restocking existing inventory.
    
    This function provides a user interface to:
    - Process inventory purchases from multiple vendors
    - Restock existing products with additional quantities
    - Add completely new products to the inventory
    - Generate purchase invoices for each vendor transaction
    - Validate user inputs to prevent data corruption
    
    The function reads existing inventory from the data file, processes user inputs,
    updates inventory data, and generates purchase invoices for record-keeping.
    
    Parameters:
        None
        
    Returns:
        None
    """
    while True:  # Outer loop for multiple vendors
        print("""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                              📦 STOCK MANAGEMENT 📦                          ║
╚═══════════════════════════════════════════════════════════════════════════════╝
""")
        display_all_products()
        # store the data from the file to data variable
        data = read_from_file()
        
        print("\n" + "─" * 50)
        print("📋 VENDOR INFORMATION")
        print("─" * 50)
        vendor_name = input("🏢 Vendor Name: ")
        print("─" * 50)
        
        # Initialize a list to store all items being processed for the invoice
        items_for_invoice = []
        

        keep_managing = True
        while keep_managing:
            try:
                print("\n" + "═" * 60)
                print("🔍 PRODUCT IDENTIFICATION")
                print("═" * 60)
                print("• Enter existing ID to restock an item")
                print("• Enter new ID to add a new product")
                print("─" * 60)
                product_id_input = input("🔢 Product ID: ")
                
                if not product_id_input.isdigit():
                    print("❌ Invalid Product ID. Please enter a number.")
                    continue
                    
                product_id = int(product_id_input)


                if product_id in data:
                    # --- RESTOCK EXISTING ITEM ---
                    item_name = data[product_id][1]
                    print("\n" + "─" * 60)
                    print("✅ RESTOCKING: Item #"+ str(product_id) + " - " + str(item_name))
                    print("─" * 60)
                    
                    # Display current information
                    print("• Current Brand: "+ str(data[product_id][2]))
                    print("• Current Quantity: "+ str(data[product_id][3]))
                    print("• Current Cost: $" + str(data[product_id][4]))
                    print("• Origin: " + str(data[product_id][5]))
                    
                    # Get new quantity with validation
                    while True:
                        new_qty_input = input("📦 Quantity to Add: ")
                        if check_digit_(new_qty_input) and int(new_qty_input) >= 0:
                            new_qty = int(new_qty_input)
                            break
                        print("❌ Invalid quantity. Please enter a non-negative number.")
                    
                    # Get new cost with validation
                    while True:
                        new_cost = input("💰 New Cost per Item: $")
                        try:
                            float_cost = float(new_cost)
                            if float_cost >= 0:
                                break
                            print("❌ Invalid cost. Please enter a non-negative number.")
                        except ValueError:
                            print("❌ Invalid cost. Please enter a valid number.")
                    
                    # Update quantity
                    old_qty = int(data[product_id][3])
                    new_total = old_qty + new_qty
                    data[product_id][3] = str(new_total)
                    # Update cost
                    data[product_id][4] = str(float_cost)
                    #update the data file
                    save_to_inventory(data)
                    #Add items to list for invoice
                    items_for_invoice.append({
                        'id': product_id,
                        'name': item_name,
                        'qty': new_qty,
                        'cost': float_cost
                    })
                    
                    print("✅ Successfully restocked " + str(new_qty) + " units of " + str(item_name))

                else:
                    # --- ADD NEW ITEM ---
                    print("\n" + "─" * 60)
                    print("🆕 ADDING NEW ITEM with ID #" + str(product_id))
                    print("─" * 60)
                    print("Please enter the details for the new product:")
                    
                    new_item_name = input("📝 Item Name: ")
                    new_item_brand = input("🏷️ Brand: ")
                    
                    # Get quantity with validation
                    while True:
                        new_item_qty_input = input("📦 Quantity: ")
                        if check_digit_(new_item_qty_input) and int(new_item_qty_input) > 0:
                            new_item_qty = int(new_item_qty_input)
                            break
                        print("❌ Invalid quantity. Please enter a positive number.")
                    
                    # Get cost with validation
                    while True:
                        new_item_cost = input("💰 Cost per Item: $")
                        try:
                            float_cost = float(new_item_cost)
                            if float_cost >= 0:
                                break
                            print("❌ Invalid cost. Please enter a non-negative number.")
                        except ValueError:
                            print("❌ Invalid cost. Please enter a valid number.")
                    
                    new_item_origin = input("🌍 Country of Origin: ")
                    data[product_id] = [
                        str(product_id),
                        new_item_name,
                        new_item_brand,
                        str(new_item_qty),
                        str(float_cost),
                        new_item_origin
                    ]
                    
                    # Add to invoice items
                    items_for_invoice.append({
                        'id': product_id,
                        'name': new_item_name,
                        'qty': new_item_qty,
                        'cost': float_cost
                    })
                    
                    print("✅ Successfully added " + str(new_item_qty) + " units of " + str(new_item_name))
                    #updating the data
                    save_to_inventory(data)

                # Ask to continue with current vendor
                print("\n" + "─" * 60)
                print("🔄 CONTINUE WITH CURRENT VENDOR?")
                print("─" * 60)
                user_input = input("Continue buying from "+  str(vendor_name) +"? (Y/N): ")
                if user_input != "y" and user_input != "Y":
                    keep_managing = False

            except ValueError:
                print("❌ Invalid input. Please enter valid numbers where required.")
            except IndexError as e:
                print("❌ Error processing data for Product ID " + str(product_id)+". Data might be corrupted."+   str(e))
            except Exception as e:
                print("❌ An unexpected error occurred: " +  str(e))

        # --- Write updated data back to file and generate invoice ---
        if items_for_invoice:
            print("\n" + "═" * 60)
            print("📊 FINALIZING TRANSACTION")
            print("═" * 60)
            
            try:
                print("\n" + "─" * 60)
                print("🧾 GENERATING INVOICE")
                print("─" * 60)
                print("Vendor: "+ str(vendor_name))
                print("Items Processed: "+ str(len(items_for_invoice)))
                
                # Generate the invoice
                buy_items_invoice(vendor_name, items_for_invoice)
                print("✅ Invoice generated successfully")
                
                # Ask if want to buy from another vendor
                print("\n" + "─" * 60)
                print("👥 CONTINUE WITH NEW VENDOR?")
                print("─" * 60)
                new_vendor = input("Want to buy from another vendor? (Y/N): ")
                if new_vendor.lower() != "y":
                    print("\n" + "─" * 60)
                    return
                # If yes the loop will continue and start again

            except IOError as e:
                print("❌ Error writing data: "+   str(e))
                return
            except Exception as e:
                print("❌ An unexpected error occurred: " +   str(e))
                return
        else:
            print("\n❗ No items were added or restocked.")
            return
        
def check_digit_(string):
    is_digit=False
    for each in string:
        try:
            int(each)
            is_digit = True
        except ValueError:
            pass
    return is_digit