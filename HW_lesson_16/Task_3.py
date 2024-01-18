#Task 3
"""
Product Store

Write a class Product that has three attributes: type, name, price
Then create a class ProductStore, which will have some Products and will operate with all products in the store. All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.

Tips: Use aggregation/composition concepts while implementing the ProductStore class. You can also implement additional classes to operate on a certain type of product, etc.

Also, the ProductStore class must have the following methods:

add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input identifiers (type or name). The discount must be specified in percentage
sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other case raises an error. It also increments income if the sell_product method succeeds.
get_income() - returns amount of many earned by ProductStore instance.
get_all_products() - returns information about all available products in the store.
get_product_info(product_name) - returns a tuple with product name and amount of items in the store.

class Product:

    pass

class ProductStore:

pass

p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)

s.add(p2, 300)

s.sell_product('Ramen', 10)

assert s.get_product_info('Ramen') == ('Ramen', 290)
"""

class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.products = {}
        self.income = 0


    def add(self, product, amount):
        if not isinstance(product, Product):
            raise ValueError("Invalid product type")

        if amount <= 0:
            raise ValueError("Amount should be greater than zero")

        if product.name not in self.products:
            self.products[product.name] = {'product': product, "amount": 0}

        self.products[product.name]["amount"] += amount


    def set_discount(self, identifier, percent, identifier_type='name'):
        if percent < 0 or percent > 100:
            raise ValueError("Discount percentage should be between 0 and 100")

        for product_info in self.products.values():
            if identifier_type == 'name' and  product_info['product'].name == identifier:
                product_info['product'].price *= (100 - percent) / 100
            elif identifier_type == 'type' and  product_info['product'].type == identifier:
                product_info['product'].price *= (100 - percent) / 100

    def sell_product(self, product_name, amount):
        if product_name not in self.products:
            raise ValueError("Product not found")

        if amount <= 0:
            raise ValueError("Amount should be greater than zero")

        if self.products[product_name]["amount"] < amount:
            raise ValueError("Not enough stock available")

        self.products[product_name]["amount"] -= amount
        self.income += amount * self.products[product_name]["product"].price



    def get_income(self):
        return self.income


    def get_all_products(self):
        all_product_info = []
        for info in  self.products.values():
            product_type = info['product'].type
            product_name =  info['product'].name
            product_price =  info['product'].price
            product_amount = info['amount']

            product_info_tuple = (product_type, product_name, product_price, product_amount)
            all_products_info.append(product_info_tuple)

        return all_products_info


    def get_product_info(self, product_name):
        if product_name in self.products:
            info = self.products[product_name]
            return (info["product"].name, info["amount"])
        else:
            return None


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell_product('Ramen', 10)
assert s.get_product_info('Ramen') == ('Ramen', 290)
            
    
            


                
            
     
        
