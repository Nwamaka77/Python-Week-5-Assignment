# Base Class: Book
class Book:
    def __init__(self, title, author, genre, pages, publication_year):
        # Initialize the book's attributes
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages
        self.publication_year = publication_year
        # Encapsulated attribute to track progress (note the underscore as a hint for internal use)
        self._current_page = 1

    def describe(self):
        """Return a formatted description of the book."""
        description = (
            f"\"{self.title}\" by {self.author}\n"
            f"Genre: {self.genre} | Pages: {self.pages} | Published: {self.publication_year}\n"
            f"Current Page: {self._current_page}"
        )
        return description

    def read(self, pages):
        """
        Simulate reading a specified number of pages:
        - Advances the current page.
        - If the page number exceeds the total pages, it sets the current page to the end.
        """
        if self._current_page >= self.pages:
            return f"You've already finished reading \"{self.title}\"!"
        self._current_page += pages
        if self._current_page >= self.pages:
            self._current_page = self.pages
            return f"You finished reading \"{self.title}\"!"
        return f"You read {pages} pages. Now you're on page {self._current_page}."

    def bookmark(self, page):
        """
        Place a bookmark by setting the current page.
        This method encapsulates the logic for safely updating the reading progress.
        """
        if page < 1 or page > self.pages:
            return f"Invalid bookmark. \"{self.title}\" only has {self.pages} pages."
        self._current_page = page
        return f"Bookmarked page {page} in \"{self.title}\"."

# Derived Class: EBook
class EBook(Book):
    def __init__(self, title, author, genre, pages, publication_year, file_format, file_size):
        # Initialize common attributes from the Book class
        super().__init__(title, author, genre, pages, publication_year)
        # Attributes unique to an eBook
        self.file_format = file_format  # e.g., EPUB, PDF, MOBI
        self.file_size = file_size      # File size in megabytes

    def describe(self):
        """
        Offer a more detailed description by including eBook-specific details.
        This demonstrates polymorphism by overriding the base method.
        """
        base_description = super().describe()
        ebook_info = f" [Digital Edition: Format: {self.file_format}, Size: {self.file_size} MB]"
        return base_description + ebook_info

    def download(self):
        """Simulate downloading the eBook."""
        return f"Downloading \"{self.title}\" in {self.file_format} format..."

# -----------------------------------------
# Demonstration of Class Usage with "The Devil Wears Prada"
# -----------------------------------------

# Creating a Book object for the physical edition of "The Devil Wears Prada"
print("=== Book Demonstration ===")
devil_book = Book("The Devil Wears Prada", "Lauren Weisberger", "Chick Lit / Fiction", 360, 2003)
print(devil_book.describe())
print(devil_book.read(100))        
print(devil_book.bookmark(150))   
print(devil_book.read(250))        
print()

# Creating an EBook object for the digital edition of "The Devil Wears Prada"
print("=== EBook Demonstration ===")
devil_ebook = EBook("The Devil Wears Prada", "Lauren Weisberger", "Chick Lit / Fiction", 360, 
                    2003, "EPUB", 1.8)
print(devil_ebook.describe())
print(devil_ebook.download())
print(devil_ebook.read(200))       
