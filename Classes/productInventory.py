"""
Name: productInventory.pi
Purpose: The application manages inventory of products.
Author: Marshall Okafor
License:

Module Dependencies: 
"""

# Create the Product class
class Product:
    
    # Initialize the attributes of the class
    def __init__(self, name, price, pId, qty):
        self.name = name
        self.price = price
        self.pId = pId
        self.qty = qty

    # Update the product's price
    def updatePrice(self, newPrice):
        if newPrice > 0:
            self.price = newPrice
        else:
            print("Error: Can not update price to lower than or equal to zero!")

    # Update the product quantity
    def updateQuantity(self, newQty, isIncrement):
        if isIncrement == True:
            self.qty += newQty
        elif (self.qty - newQty) >= 0:
            self.qty -= newQty
        else:
            print("Error: Can not reduce quantity further!")

    # Return the quantity of the product
    def getQuantity(self):
        return self.qty

    # Display the product information
    def viewProduct(self):
        print("Product ID: " + str(self.pId) + ", Name: " + self.name + ", Price: " + str(self.price) + ", Quantity: " + str(self.qty))

# Create the Inventory class
class Inventory:
    # Initiate the attribute
    def __init__(self):
        self.listProduct = []

    # Add new product to the Inventory
    def addProduct(self, pId):
        self.listProduct.append(pId)

    # Remove product from the Inventory
    def removeProduct(self, pId):
        if pId in self.listProduct:
            self.listProduct.remove(pId)
        else:
            print("Error: Product ID is not in the inventory!")

    # Display the content of the inventory
    def viewInventory(self):
        print(self.listProduct)

# Main program to run
if __name__ == '__main__':
    prod1 = Product("colgate", 2.20, 1, 5)
    print(prod1.getQuantity())
    prod1.updateQuantity(2, True)
    prod1.viewProduct()

    invent1 = Inventory()
    invent1.addProduct(1)
    #invent1.removeProduct(2)
    invent1.viewInventory()
