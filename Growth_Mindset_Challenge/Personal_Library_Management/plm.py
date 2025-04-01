#Libraries
import json
import os
import time

#Making a class for PLM work
class PersonalLibraryManager:
    def __init__(self, filename="library.plm"):
        """Initialize the library and load data from file."""
        self.filename = filename
        self.library = self._load_library()

    def _load_library(self):
        """Load library data from a file (handles errors gracefully)."""
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def _save_library(self):
        """Save the current library state to a file."""
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.library, file, indent=4)

    def _display_header(self, title):
        """Display a formatted section header."""
        print("\n" + "=" * 50)
        print(f"{title.center(50)}")
        print("=" * 50)

    def add_book(self):
        """Add a new book to the library."""
        self._display_header("📖 Add a New Book")
        title = input("Title: ").strip()
        author = input("Author: ").strip()
        year = self._get_int_input("Publication Year: ")
        genre = input("Genre: ").strip()
        read_status = self._confirm_input("Have you read it? (y/n): ")

        book = {
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read": read_status
        }
        self.library.append(book)
        self._save_library()
        print(f'✅ Book "{title}" added successfully!')

    def remove_book(self):
        """Remove a book by title."""
        self._display_header("🗑 Remove a Book")
        title = input("Enter the title of the book to remove: ").strip()
        for book in self.library:
            if book["title"].lower() == title.lower():
                self.library.remove(book)
                self._save_library()
                print(f'✅ Book "{title}" removed successfully!')
                return
        print("⚠ Book not found.")

    def edit_book(self):
        """Edit book details."""
        self._display_header("✏️ Edit Book Details")
        title = input("Enter the title of the book to edit: ").strip()
        for book in self.library:
            if book["title"].lower() == title.lower():
                print("Editing book details (leave blank to keep current value).")
                book["title"] = self._get_new_value("New Title", book["title"])
                book["author"] = self._get_new_value("New Author", book["author"])
                book["year"] = self._get_int_input("New Year", book["year"])
                book["genre"] = self._get_new_value("New Genre", book["genre"])
                book["read"] = self._confirm_input("Have you read it? (y/n): ", book["read"])
                self._save_library()
                print(f'✅ Book "{title}" updated successfully!')
                return
        print("⚠ Book not found.")

    def search_book(self):
        """Search for books by title or author (partial match)."""
        self._display_header("🔍 Search for a Book")
        query = input("Enter title or author: ").strip().lower()
        matches = [book for book in self.library if query in book["title"].lower() or query in book["author"].lower()]

        if matches:
            self._display_books(matches)
        else:
            print("⚠ No matching books found.")

    def display_all_books(self):
        """Display all books in the library."""
        self._display_header("📚 Your Library Collection")
        if not self.library:
            print("No books available.")
        else:
            self._display_books(self.library)

    def display_statistics(self):
        """Display statistics about the library."""
        self._display_header("📊 Library Statistics")
        total_books = len(self.library)
        if total_books == 0:
            print("No books in the library.")
            return

        read_books = sum(1 for book in self.library if book["read"])
        percentage_read = (read_books / total_books) * 100
        print(f"Total Books: {total_books}")
        print(f"Books Read: {read_books} ({percentage_read:.2f}% read)")

    def _display_books(self, books):
        """Display books in a structured format."""
        for idx, book in enumerate(books, 1):
            read_status = "✔ Read" if book["read"] else "❌ Unread"
            print(f"\n{idx}. 📖 {book['title']} ({book['year']})")
            print(f"   ✏️ Author: {book['author']}")
            print(f"   🎭 Genre: {book['genre']}")
            print(f"   📌 Status: {read_status}")

    def _get_int_input(self, prompt, default=None):
        """Safely get an integer input with an optional default value."""
        while True:
            value = input(prompt + (f" (default: {default})" if default else "") + ": ").strip()
            if value == "" and default is not None:
                return default
            if value.isdigit():
                return int(value)
            print("⚠ Invalid input. Please enter a number.")

    def _get_new_value(self, prompt, current_value):
        """Get a new value from the user, or return the existing value if left blank."""
        value = input(f"{prompt} (current: {current_value}): ").strip()
        return value if value else current_value

    def _confirm_input(self, prompt, default=False):
        """Confirm input as boolean (yes/no)."""
        value = input(prompt).strip().lower()
        return True if value == "y" else False if value == "n" else default

    def run(self):
        """Run the interactive CLI menu."""
        while True:
            self._display_header("📚 Personal Library Manager")
            print("1️⃣ Add a Book")
            print("2️⃣ Remove a Book")
            print("3️⃣ Edit a Book")
            print("4️⃣ Search for a Book")
            print("5️⃣ Display All Books")
            print("6️⃣ View Statistics")
            print("7️⃣ Exit")

            choice = input("Choose an option: ").strip()
            options = {
                "1": self.add_book,
                "2": self.remove_book,
                "3": self.edit_book,
                "4": self.search_book,
                "5": self.display_all_books,
                "6": self.display_statistics,
                "7": exit
            }

            action = options.get(choice)
            if action:
                action()
                time.sleep(1)  # Add a small delay for better user experience
            else:
                print("⚠ Invalid choice. Try again.")

if __name__ == "__main__":
    manager = PersonalLibraryManager()
    manager.run()
