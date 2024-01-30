
class Inventory:
    def __init__(self):
        self.products= []
        self.category= []

    def add_product(self,product):
        self.products.append(product)
        return product
    def add_cat(self,category_name):
        self.category.append(category_name)

    def remove_product(self,product):
        self.products.remove(product)


    def display_inventory(self):
        for p in self.products:
            print(f'{p.Name} ')
        return 'this all products here '

    def display_cat(self):
        for c in self.category:
            print(f'{c.name}')
        return 'this is all category here'

