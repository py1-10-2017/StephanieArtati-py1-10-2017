from product import Product
from store import Store

Product1 = Product(20,"Toddler shoes",1, "Carter's","for sale")
Product2 = Product(10,"Toddler socks",1, "Carter's","for sale")
Product1.sell()
Product2.sell()
Product2.return_product("used")

Store1 = Store([Product1, Product2], "Redmond", "Stephanie Artati")
Product3 = Product(25,"Toddler sleepsack",2, "Gymboree","for sale")
Store1.add_product(Product3)
Store1.inventory()

Store1.remove_product("Toddler socks")
Store1.inventory()
