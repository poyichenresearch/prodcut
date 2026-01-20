import os

products = []

## read in file
if os.path.isfile('products.csv'):
	print('yes')
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name,price = line.strip().split(',')
			products.append([name,price])
	print(products)

else:
	print('cannot find it')

## user enter:
while True:
	name = input('pls enter the name of the product: ')
	if name == 'q':
		break
	price = input('enter the price of this product: ')
	products.append([name,price])
print(products)

# print out results
for p in products:
	print(p)

with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
