import os

def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name,price = line.strip().split(',')
			products.append([name,price])
	print(products)
	return products

## user enter:
def user_input(products):
	while True:
		name = input('pls enter the name of the product: ')
		if name == 'q':
			break
		price = input('enter the price of this product: ')
		products.append([name,price])
	print(products)
	return(products)

# print out results
def print_products(products):
	for p in products:
		print(p)

def write_files(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

def main(filename):
	if os.path.isfile(filename):
		print('yes')
		products = read_file(filename)
	else:
		print('cannot find it')

	products = user_input(products)
	print_products(products)
	write_files(filename, products)

main("products.csv")