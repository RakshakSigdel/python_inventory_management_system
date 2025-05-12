"""
WeCare Inventory Management System - File Operations Module

This module manages inventory data persistence and document generation:
1. Inventory Management: Handles saving inventory data with automatic removal
   of out-of-stock items (quantity < 1)
2. Purchase Documentation: Generates professional purchase invoices when buying
   new inventory items from vendors
3. Sales Documentation: Creates detailed customer sales invoices with support for
   promotions like "Buy 3 Get 1 Free"

All invoice files are saved in organized directories with timestamps for easy retrieval.

Author: [Rakshak Sigdel]
Version: 1.0
"""

from datetime import datetime

def save_to_inventory(data):
    """
    Save inventory data to file with error handling.
    Removes items with quantity less than 1.
    
    The data is saved in the format:
    ID,Product Name,Brand,Quantity,Price,Country
    """
    try:
        for key in list(data.keys()):
            try:
                if int(data[key][3]) < 1:
                    data.pop(key)
            except (ValueError, IndexError):
                print("⚠️ Warning: Invalid quantity data for product ID " + {key})
        
        # Write the filtered data to file
        with open('products.txt', 'w') as f:
            for key in (data.keys()):
                f.write(','.join(str(field).strip() for field in data[key]) + '\n')
        
        
        print("✅ Inventory data updated successfully")
    except IOError as e:
        print("❌ Error writing to file: " + {e})
    except Exception as e:
        print("❌ An unexpected Error occured while writing to file: " + {e})

def buy_items_invoice(vendor_name, items_list):
    """
    Generates a professional purchase invoice for inventory transactions.
    
    This function creates a formatted text file containing a detailed invoice
    for items purchased from a vendor. The invoice includes:
    - Vendor information
    - Date and time of purchase
    - Unique invoice number
    - Detailed listing of all purchased items
    - Quantity, tax and cost calculations
    - Total purchase amount
    - Contact information
    
    Parameters:
        vendor_name (str): The name of the vendor supplying the items
        items_list (list): A list of dictionaries containing item details
                          Each dict contains 'id', 'name', 'qty', and 'cost'
        
    Returns:
        None: The function writes the invoice to a file but does not return a value
    """
    try:
        # Calculate total cost with tax for all items
        buy_price = 0
        for item in items_list:
            qty = int(item['qty'])
            cost = float(item['cost'])
            buy_price += qty * cost

        tax_amount = buy_price * 0.13  # Fixed: calculate tax based on buy_price
        total_cost = buy_price + tax_amount
        
       # Get current date and time for invoice
        now = datetime.now()

        current_date = str(now.year) + "-" + str(now.month) + "-" + str(now.day)
        current_time = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
        invoice_number = str(now.year) + str(now.month) + str(now.day) + "-" + str(now.hour) + str(now.minute) + str(now.second)
        
        invoice_content = f"""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                           ✦ WⒺ CARE Vendor ✦                               ║
║                         OFFICIAL PURCHASE INVOICE                            ║
║                                                                              ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  📄 Invoice #: {invoice_number}                                              ║ 
║  📅 Date: {current_date}                           🕒 Time: {current_time}     ║ 
║  🏢 Vendor: {vendor_name}                                                   ║  
║                                                                              ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                             PRODUCT DETAILS                                  ║
╠═════════════════════════════════════════════════════════════════════════════╣
"""
        
        index = 0
        length = len(items_list)
        while index < length:
            item = items_list[index]
            item_cost = int(item['qty']) * float(item['cost'])
            invoice_content += f"""║                                                                              ║\n║  Item {index+1}                                                                     ║\n║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  ║\n║  Product ID: #{item['id']}                                                  ║  \n║  Product Name: {item['name']}                                                ║ \n║                                                                              ║\n║  Quantity: {item['qty']} units    ×    Unit Cost: ${float(item['cost']):.2f}           \n║                                                Subtotal: ${item_cost:.2f}     \n║                                                                              ║\n"""
            if index < length - 1:
                invoice_content += "╠══════════════════════════════════════════════════════════════════════════════╣\n"
            index += 1
        
        invoice_content += f"""╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  💰 Items Worth:                                         ${buy_price:.2f}    
║  💰 Tax Amount:                                          ${tax_amount:.2f}    
║  💰 TOTAL COST:                                          ${total_cost:.2f}    
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  Payment Terms: Due on receipt                                               ║
║  For questions regarding this invoice, please contact:                       ║
║  📧 accounting@wecare.com | 📞 (555) 123-4567                               ║
║                                                                              ║
║                     THANK YOU FOR YOUR BUSINESS!                             ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
        
            
        # Write to file with UTF-8 encoding
        with open('purchase_' + invoice_number +'.txt', 'w', encoding='utf-8') as f:
            f.write(invoice_content)
            
        print("✅ Invoice generated Successfully: purchase_" + invoice_number + ".txt")
        
    except Exception as e:
        print("❌ Error generating invoice: " + str(e))
        


def sell_item_invoice(customer_name, items_for_invoice):
    """
    Generates a professional sales invoice for customer purchases.

    Parameters:
        customer_name (str): The name of the customer making the purchase
        items_for_invoice (list): A list of lists containing item details
                                 Each list contains [product_id, product_name,
                                 quantity, free_product, total_cost, unit_cost]

    Returns:
        None
    """
    try:
        # Calculate total cost for all items
        total_cost = 0
        for item in items_for_invoice:
            total_cost += item[4]
        tax_amount = total_cost * 0.13  
        total_amount = total_cost + tax_amount 
        # Get current date and time for invoice
        now = datetime.now()

        current_date = str(now.year) + "-" + str(now.month) + "-" + str(now.day)
        current_time = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
        invoice_number = str(now.year) + str(now.month) + str(now.day) + "-" + str(now.hour) + str(now.minute) + str(now.second)

        # Build the invoice content
        invoice_content = f"""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                           ✦ WⒺ CARE  vendor✦                               ║
║                          OFFICIAL SALES INVOICE                             ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║  📄 Invoice #: {invoice_number}                                                ║ 
║  📅 Date: {current_date}                           🕒 Time: {current_time}             ║  
║  👤 Customer: {customer_name}                                                  
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                             PRODUCT DETAILS                                 ║
╠═════════════════════════════════════════════════════════════════════════════╣
"""

        index = 0
        length = len(items_for_invoice)
        while index < length:
            item = items_for_invoice[index]
            invoice_content += f"""║                                                                             ║
║  Item {index + 1}                                                                     ║
║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━║
║  Product ID: #{item[0]}                                                                     
║  Product Name: {item[1]}                                         
║  Brand Name: {item[6]}                                         
║                                                                              
║  Quantity: {item[2]} units    ×    Unit Cost: ${item[5]:.2f}      
║                                                Subtotal: ${item[4]:.2f}     
║  🎁 Free Products: {item[3]} units (Buy 3 Get 1 Free)             
║                                                                              
"""
            if index < length - 1:
                invoice_content += "╠═════════════════════════════════════════════════════════════════════════════╣\n"
            index += 1

        invoice_content += f"""╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║  💰 TOTAL COST:                                          ${total_cost:.2f} 
║  💰 Tax Amount:                                          ${tax_amount:.2f} 
║  💰 TOTAL Amount:                                          ${total_amount:.2f} 
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║  Payment Terms: Due on receipt                                              ║
║  For questions regarding this invoice, please contact:                      ║
║  📧 support@wecare.com | 📞 (555) 987-6543                                 ║
║                                                                             ║
║                THANK YOU FOR CHOOSING WE CARE MEDICAL!                      ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
"""

        # Write to file with UTF-8 encoding
        with open('sell_'+invoice_number + '.txt', 'w', encoding='utf-8') as f:
            f.write(invoice_content)

        print("✅ Invoice generated Successfully: sell_" + invoice_number + ".txt")

    except Exception as e:
        print("❌ Error generating invoice: " + str(e))
