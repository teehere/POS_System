# Point Of Sales System (POS)

## Introduction
This project is aim to develop a **point-of-sales (POS) system** for a retail shop that can be used to generate the invoice or receipt of a transaction

## Project Overview
1.	**Item Master Module**
    - Create, Read, Update and Delete (CRUD) any details of an item and save it in a text file
     
2. **Sales Module**
   - Allow the user to enter items bought by customer to the counter
   - The system capture all item codes and retrieve the description and price from Item Master
   - Calculate the total amount to be paid for the transaction and to round it to the nearest 5 cents
     
3. **Membership and payment process**
    - Membership for discount or reward
    - The discount rates given based on the type of membership in which the customer is subscribed to. <br /> The membership types: Premium, Gold, and Normal with a discount rate of 20%, 10% and 5% respectively
    - Customers are allowed to choose to pay by using cash, credit card, or eWallet

4. **Inventory Module**
    - Upkeep of the inventory level
    - Request for items to be added when stock level falls under the safety stock level

## Project Structure 
```bash
ABC_Retail_System/
│
├── menu.py                 # Main entry point
├── Maintenance.py          # Core file operations & item CRUD
├── membership.py           # Membership management
├── StockManage.py          # Inventory management
├── Sales.py                # Sales transactions
├── report.py               # Sales reports & analytics
│
├── assfile.txt             # Items: Code|Name|Price|Stock
├── member.txt              # Members: Name|Type|PaymentMethod
├── receipt.txt             # Sales records
└── itemSold.txt            # Current cart items
```

## Credits
This Project is developed by:
- Tee Le Xuan - Membership maintenance and report
- Wong Zern Ye - Main menu
- Lim Lei Shuen - Sales
- Chan Jia Ying - Stock management
- Chio Xi Wen - Item maintenance
