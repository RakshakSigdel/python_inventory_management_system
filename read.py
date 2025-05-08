"""
WeCare Inventory Management System - Read Module

This module handles reading inventory data from the data file and preparing it for use
within the system. It processes data from a comma-separated text file where each line
represents a product entry with the first field being the product ID.

Features:
- Reads structured product data from data/data.txt
- Validates data format during import
- Handles file access errors gracefully
- Returns data in a dictionary structure for easy lookup by ID

Author: Rakshak Sigdel
Version: 1.0
"""

def read_from_file():
    """
    Reads product data from the data file.
    
    This function reads data from the data file and stores it in a dictionary
    with ID as the key and product details as values.
    
    Returns:
        dict: Dictionary containing inventory data with ID as key
    """
    # Dictionary to store inventory data with ID as key
    data = {}

    try:
        # Read data from file and store in dictionary
        with open('products.txt', 'r') as f:
            for line in f:
                if line.strip():  # Skip empty lines
                    fields = line.strip().split(',')
                    if fields:
                        try:
                            # Use the first field as ID
                            id_value = int(fields[0])
                            # Store all fields the data dictionary
                            data[id_value] = fields
                        except ValueError:
                            print(f"⚠️ Invalid ID format in line: {line.strip()}")
    except FileNotFoundError:
        print("⚠️ Data file not found. Starting with an empty inventory.")
    except Exception as e:
        print("❌ Error reading data file: " +  str({e}))
    
    return data
