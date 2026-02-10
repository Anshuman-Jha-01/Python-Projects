class Library:
    def __init__(self):
        # Initialize the library with zero books and an empty dictionary
        self.no_of_books = 0
        self.books = {}
    
    def add_book(self, author, name):
        """
        Add a book to the library under the given author.
        Increments the total book count and organizes books by author.
        """
        self.no_of_books += 1
        if author in self.books:
            self.books[author].append(name)
        else:
            self.books[author] = [name]
        
        print("\n📚 Book successfully added to the Library!\n")
    
    def get_no_of_books(self):
        """
        Return the total number of books in the library.
        """
        return self.no_of_books
    
    def check_consistency(self):
        """
        Verify that the number of books recorded matches the actual count.
        Returns True if consistent, False otherwise.
        """
        num_book = 0
        keys = self.books.keys()
        for key in keys:
            num_book += len(self.books.get(key))
        if num_book==self.no_of_books:
            return True
        else:
            return False
    
    def print_books(self):
        """
        Display all books in the library, grouped by author.
        Provides a clean and user-friendly output.
        """
        print("\n📖 Library Catalog")
        print("=" * 40)
        print(f"Total number of books: {self.no_of_books}\n")
        
        if self.no_of_books == 0:
            print("⚠️ The library is currently empty.")
        else:
            for author, titles in self.books.items():
                print(f"👤 Author: {author}")
                for idx, title in enumerate(titles, start=1):
                    print(f"   {idx}. {title}")
                print("-" * 40)  # Separator for clarity
