from models import Category, Product, User, Status, Order, Order_item


category = Category(name='Laptop')
category.save()
category = Category(name='Smartphone')
category.save()
category = Category(name='Smartwatch')
category.save()
category = Category(name='Tablet')
category.save()

product = Product(title='ASUS TUF Gaming', description='Intel Core i7 11800H', category_id=1)
product.save()
product = Product(title='Apple Macbook Pro 14', description='Apple M1 Pro', category_id=1)
product.save()
product = Product(title='HP Victus', description='AMD Ryzen 5 5600H', category_id=1)
product.save()
product = Product(title='Lenovo Legion 5', description='Intel Core i7 11800H', category_id=1)
product.save()
product = Product(title='Xiaomi 12T Pro', description='Qualcomm Snapdragon 8+ Gen1', category_id=2)
product.save()
product = Product(title='Apple iPhone 14', description='Apple A15 Bionic', category_id=2)
product.save()
product = Product(title='Samsung Galaxy S22', description='Exynos 2200', category_id=2)
product.save()
product = Product(title='Apple Watch SE 40', description='iOS', category_id=3)
product.save()
product = Product(title='Apple Watch SE Nike', description='iOS', category_id=3)
product.save()
product = Product(title='Samsung Galaxy Watch 4', description='Android', category_id=3)
product.save()
product = Product(title='Honor Pad 8', description='Qualcomm Snapdragon 680', category_id=4)
product.save()
product = Product(title='Apple iPad mini', description='Apple A15 Bionic', category_id=4)
product.save()
product = Product(title='Apple iPad Air', description='Apple M1', category_id=4)
product.save()
product = Product(title='Xiaomi Redmi', description='MediaTek Helio G99', category_id=4)
product.save()
product = Product(title='Xiaomi Pad 5', description='', category_id=4)
product.save()

user = User(name='Alex', email='a.ivanov@mail.com')
user.save()
user = User(name='Ann', email='ann87@gmail.com')
user.save()
user = User(name='Nick', email='Nixs@tut.by')
user.save()
user = User(name='Maksim', email='Max_lite@gmail.com')
user.save()
user = User(name='Vasya', email='v.smirnoff@gmail.com')
user.save()

status = Status(name='active')
status.save()
status = Status(name='deactive')
status.save()
status = Status(name='registr.')
status.save()

order = Order(user_id=1, status_id=1)
order.save()
order = Order(user_id=2, status_id=2)
order.save()
order = Order(user_id=3, status_id=1)
order.save()
order = Order(user_id=4, status_id=1)
order.save()
order = Order(user_id=5, status_id=3)
order.save()

order_item = Order_item(order_id=1, product_id=1)
order_item.save()
order_item = Order_item(order_id=1, product_id=2)
order_item.save()
order_item = Order_item(order_id=2, product_id=3)
order_item.save()
order_item = Order_item(order_id=3, product_id=3)
order_item.save()
order_item = Order_item(order_id=4, product_id=3)
order_item.save()
order_item = Order_item(order_id=1, product_id=4)
order_item.save()
order_item = Order_item(order_id=3, product_id=5)
order_item.save()
order_item = Order_item(order_id=4, product_id=6)
order_item.save()
order_item = Order_item(order_id=1, product_id=7)
order_item.save()
order_item = Order_item(order_id=2, product_id=7)
order_item.save()
order_item = Order_item(order_id=1, product_id=8)
order_item.save()
order_item = Order_item(order_id=3, product_id=8)
order_item.save()
order_item = Order_item(order_id=1, product_id=9)
order_item.save()
order_item = Order_item(order_id=3, product_id=10)
order_item.save()
order_item = Order_item(order_id=2, product_id=11)
order_item.save()
order_item = Order_item(order_id=4, product_id=11)
order_item.save()
order_item = Order_item(order_id=2, product_id=12)
order_item.save()
order_item = Order_item(order_id=1, product_id=13)
order_item.save()
order_item = Order_item(order_id=3, product_id=13)
order_item.save()
order_item = Order_item(order_id=2, product_id=14)
order_item.save()
order_item = Order_item(order_id=1, product_id=15)
order_item.save()