from Product import *
from Category import *
from inventory import *
from Report import *


Inv = Inventory()

product1 = Product('Cola','50$','2023',19088,'drinks')
product2 = Product('Pepsi','30$','2023',15088,'drinks')
product3 = Product('water','20$','2023',50088,'drinks')


print(product1.display_info())
print(product2.display_info())

print('-----------------------------------------------------------------')

Inv.add_product(product1)
Inv.add_product(product2)
Inv.add_product(product3)


print(Inv.display_inventory())


print('---------------------------------------------------------------')

Inv.remove_product(product2)
print(Inv.display_inventory())

print('---------------------------------------------------------------')

cat1 = Category('Drinks')
cat2 = Category('Clothes')

Inv.add_cat(cat1)
Inv.add_cat(cat2)

print(Inv.display_cat())

print('------------------------------------------------------')

R1 = Reports()
R1.report(Inv)
print('---------------------------------------------------------')

R2 = Reports()
R2.category_report(Inv)


print('----------------------------------------------------------')


