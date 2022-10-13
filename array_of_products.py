def arrayOfProducts(array):
    # Write your code here.
    products = [1 for _ in range(len(array))]
    left_products = [1 for _ in range(len(array))]
    right_products = [1 for _ in range(len(array))]

    left_running_product = 1
    for i in range(0, len(array)):
        left_products[i] = left_running_product
        left_running_product *= array[i]

    right_running_product = 1
    for i in reversed(range(len(array))):
        right_products[i] = right_running_product
        right_running_product *= array[i]

    for i in range(len(array)):
        products[i] = left_products[i] * right_products[i]

    return products
    

if __name__ == "__main__":
    array = [5, 1, 4, 2]
    p = arrayOfProducts(array)
    print(p)