import csv

def add():
    f = open("product.csv", "a", newline="")
    w = csv.writer(f)

    n = int(input("Enter the number of products: "))

    for i in range(n):
        print("\nEnter details of product", i + 1)

        pid = int(input("Enter product id: "))
        pname = input("Enter product name: ")
        price = float(input("Enter product price: "))

        record = [pid, pname, price]
        w.writerow(record)

    f.close()
    print("Records added successfully.")

def search():
    f = open("product.csv", "r")
    r = csv.reader(f)

    for rec in r:
        if float(rec[2]) > 10000:
            print("Product ID:", rec[0])
            print("Product Name:", rec[1])
            print("Product Price:", rec[2])
            print()

    f.close()


add()
search()