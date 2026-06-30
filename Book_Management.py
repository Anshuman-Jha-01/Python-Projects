import pickle

#Book Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

#Booklist
bookList = {}

#Fetch book list from file
try:
    f = open("books.pickle", "rb")
    bookList = pickle.load(f)
    f.close()
except Exception as e:
    pass

print("----Welcome to Book Management System----")
print("Select an option:")
print("1. View Book List")
print("2. Add a Book")
print("3. Remove a Book (Based on Book Title)")
print("4. Quit")

cont = True

while cont:
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            if(len(bookList)!=0):
                for idx, book in enumerate(bookList.values(), start=1):
                    print(idx, "->", "Title:", book.title, ", Author:", book.author)
            else:
                print("No books present in the book list")
        case 2:
            title = input("Enter book title: ")
            author = input("Enter book author name: ")
            book = Book(title, author)
            bookList.update({title.lower(): book})
            print("Book Added successfully!")
        case 3:
            title = input("Enter the book title: ")
            if title.lower() in bookList:
                try:
                    bookList.pop(title.lower())
                    print("Book Removed!")
                except:
                    print(e)
                else:
                    f = open("books.pickle", "wb")
                    pickle.dump(bookList, f)
            else:
                print("Book with the given title does not exist in the book list.")
        case 4:
            cont = False
            f = open("books.pickle", "wb")
            pickle.dump(bookList, f)
            print("Exiting...")
        case _:
            print("Invalid Choice. Please select a valid option (1, 2, 3).")
        