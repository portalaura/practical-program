import pickle

def create_file():
    f = open("book.dat", "ab")

    n = int(input("Enter the number of books: "))

    for i in range(n):
        print("\nEnter details of book", i + 1)

        book = {}
        book['bid'] = int(input("Enter book id: "))
        book['bname'] = input("Enter book name: ")
        book['author'] = input("Enter author name: ")
        book['price'] = float(input("Enter price: "))

        pickle.dump(book, f)
    f.close()
    print("Records added successfully.")

def count_rec(author):
    f = open("book.dat", "rb")
    count = 0

    try:
        while True:
            book = pickle.load(f)
            if book['author'].lower() == author.lower():
                count += 1
    except EOFError:
        pass

    f.close()
    return count


create_file()

a = input("\nEnter author name to search: ")
print("Number of books by", a, "=", count_rec(a))