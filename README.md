# WeCare Inventory Management System

## Overview

WeCare Inventory Management System is a command-line application designed to help manage inventory for a retail or medical supply business. It allows users to display current inventory, process sales (with a "Buy 3 Get 1 Free" promotion), restock items, and generate professional invoices for both sales and purchases.

> **Note:** This project was developed as part of a university coursework assignment. The implementation closely follows the provided guidelines and requirements, which may have resulted in some limitations and lack of certain advanced functionalities or optimizations. The code prioritizes meeting assignment criteria over production-level robustness or extensibility.

## Features

- **Display Inventory:** View all products in a formatted table with details such as ID, name, brand, quantity, cost, and origin.
- **Sales Management:** Sell items to customers, apply the "Buy 3 Get 1 Free" promotion, update inventory, and generate sales invoices.
- **Stock Management:** Restock existing products or add new items, update inventory, and generate purchase invoices for vendors.
- **Invoice Generation:** Automatically create detailed, professional invoices for both sales and purchases, saved as text files.
- **User-Friendly CLI:** Simple menu-driven interface for easy navigation and operation.

## Limitations

- The program was developed strictly according to coursework guidelines, which may have led to:
  - Limited error handling and input validation.
  - Some features being implemented in a basic or non-optimal way.
  - Lack of advanced features such as user authentication, reporting, or a graphical interface.
  - Some code duplication and lack of modularity.
- The inventory data is stored in a plain text file (`products.txt`), which is not suitable for large-scale or concurrent use.

## Getting Started

### Prerequisites
- Python 3.x
- No external libraries required (uses only Python standard library)

### Installation
1. Clone this repository or download the source code files.
2. Ensure all files (`main.py`, `operation.py`, `read.py`, `write.py`, and `products.txt`) are in the same directory.

### Usage
1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the program:
   ```
   python main.py
   ```
4. Follow the on-screen menu to interact with the system.

### File Structure
- `main.py` - Entry point; handles user interaction and menu navigation.
- `operation.py` - Core business logic for inventory, sales, and restocking.
- `read.py` - Handles reading inventory data from file.
- `write.py` - Handles writing inventory data and generating invoices.
- `products.txt` - Inventory data file (CSV format).


## Author
- Rakshak Sigdel

## License
This project is for educational purposes only and is not intended for commercial use.

## Acknowledgements
- Developed as part of university coursework.
- Special thanks to course instructors for guidance and requirements.

---

*For any questions or suggestions, please contact the author or open an issue on GitHub.*
