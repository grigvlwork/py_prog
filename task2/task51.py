stores = dict()
products = dict()
while True:
    try:
        s = input()
        store, prod = s.split(":")
        products_list = prod.split(",")
        prod_in_store = list()
        for item in products_list:
            product, amount = item.split("-")
            amount = int(amount)
            prod_in_store.append((product, amount))
            if products.get(product) is None:
                products[product] = amount
            else:
                products[product] += amount
        stores[store] = prod_in_store
    except EOFError:
        break
min_amount = 9999999999999999999999
min_prod = ""
for key in products:
    if min_amount > products[key]:
        min_amount = products[key]
        min_prod = key
print(min_prod, ":")
sum = 0
for key in stores:
    for t in stores[key]:
        if min_prod == t[0]:
            print(key, '-', t[1])
            sum += t[1]
print("Итого: ", sum)
