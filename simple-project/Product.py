class Product:
    def __init__(self, name, price, model, id, category):
        self.Name = name
        self.Price = price
        self.Model = model
        self.Id = id
        self.Category = category

    def display_info(self):
        return f' name is {self.Name} - price{self.Price} - model {self.Model} - id {self.Id} - category {self.Category}   '


