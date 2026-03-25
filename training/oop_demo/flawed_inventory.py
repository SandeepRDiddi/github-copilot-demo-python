"""Intentionally flawed Python code for a Copilot review-and-fix demo."""


class product:
    def __init__(self,name,price,stock=0):
        self.name=name
        self.price=price
        self.stock=stock

    def AddStock(self,amount):
        self.stock=self.stock+amount

    def Sell(self,quantity):
        if quantity > self.stock:
            raise ValueError("not enough stock")
        self.stock=self.stock-quantity
        return self.price*quantity


class inventorymanager:
    def __init__(self,items=[]):
        self.items=items

    def add_product(self,name,price,stock):
        self.items.append({"name":name,"price":price,"stock":stock})

    def total_inventory_value(self):
        total=0
        for item in self.items:
            total=total+(item["price"]*item["stock"])
        return total

    def sell_product(self,name,quantity):
        for item in self.items:
            if item["name"]==name:
                if quantity > item["stock"]:
                    raise ValueError("not enough stock")
                item["stock"]=item["stock"]-quantity
                return item["price"]*quantity
        raise ValueError("product not found")
