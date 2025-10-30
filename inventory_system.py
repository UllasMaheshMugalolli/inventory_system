"""
Inventory management system module.

This module provides functions to manage stock data including adding,
removing, loading, saving, and reporting on inventory items.
"""
import json
from datetime import datetime

# Global variable
stock_data = {}

def add_item(item="default", qty=0, logs=None):
    """
    Add an item to the inventory.
    
    Args:
        item: The item name to add
        qty: The quantity to add
        logs: Optional list to append log messages to
    """
    if logs is None:
        logs = []
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{str(datetime.now())}: Added {qty} of {item}")

def remove_item(item, qty):
    """
    Remove an item from the inventory.
    
    Args:
        item: The item name to remove
        qty: The quantity to remove
    """
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        pass

def get_qty(item):
    """
    Get the quantity of an item in inventory.
    
    Args:
        item: The item name to query
        
    Returns:
        The quantity of the item
    """
    return stock_data[item]

def load_data(file="inventory.json"):
    """
    Load inventory data from a JSON file.
    
    Args:
        file: The file path to load from
    """
    global stock_data  # pylint: disable=global-statement
    with open(file, "r", encoding="utf-8") as f:
        stock_data = json.loads(f.read())

def save_data(file="inventory.json"):
    """
    Save inventory data to a JSON file.
    
    Args:
        file: The file path to save to
    """
    with open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(stock_data))

def print_data():
    """
    Print the current inventory report.
    """
    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])

def check_low_items(threshold=5):
    """
    Check for items below a quantity threshold.
    
    Args:
        threshold: The quantity threshold to check against
        
    Returns:
        List of items below the threshold
    """
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result

def main():
    """
    Main function to demonstrate inventory system functionality.
    """
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")  # invalid types, no check
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    print('eval used')  # fixed: removed dangerous eval

main()