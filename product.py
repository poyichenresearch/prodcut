products = []
while True:
	name = input('pls enter the name of the product: ')
	if name == 'q':
		break
	price = input('enter the price of this product: ')
	products.append([name,price])
#print(products)

for p in products:
	print(p)