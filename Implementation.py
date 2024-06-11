import json
import csv

# File paths
BOOKS_FILE = 'BOOK MANAGEMENT APPLICATION/books.json'
TITLES_CSV_FILE = 'BOOK MANAGEMENT APPLICATION/titles.csv'
YEARS_CSV_FILE = 'BOOK MANAGEMENT APPLICATION/years.csv'

# Load books data from JSON file
def load_books():
    try:
        with open(BOOKS_FILE, 'r') as file:
            data = json.load(file)
            if isinstance(data, dict):
                return data
            else:
                print("Error: JSON data is not in the expected dictionary format.")
                return {}
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Error: JSON file is malformed.")
        return {}

# Save books data to JSON file
def save_books(books):
    with open(BOOKS_FILE, 'w') as file:
        json.dump(books, file, indent=4)

# Add a new book to the collection
def add_book(books):
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    genre = input("Enter book genre: ")
    year = input("Enter publication year: ")
    price = input("Enter book price: ")

    try:
        year = int(year)
    except ValueError:
        print("Invalid year. Please enter a valid integer.")
        return

    try:
        price = float(price)
        if price < 0:
            raise ValueError("Price cannot be negative.")
    except ValueError:
        print("Invalid price. Please enter a valid positive number.")
        return

    book_id = str(len(books) + 1)
    books[book_id] = {'title': title, 'author': author, 'genre': genre, 'year': year, 'price': price}
    save_books(books)
    print("Book added successfully.")

# View all books in the collection
def view_books(books):
    if not books:
        print("No books available.")
        return

    for book_id, details in books.items():
        title = details.get('title', 'Unknown Title')
        author = details.get('author', 'Unknown Author')
        genre = details.get('genre', 'Unknown Genre' )
        year = details.get('year', 'Unknown Year')
        price = details.get('price', 0.0)
        print(f"{book_id}. Title: {title}, Author: {author}, Genre: {genre}, Year: {year}, Price: ${price:.2f}")

# Extract book titles to a CSV file
def extract_titles(books):
    titles = [details['title'] for details in books.values()]
    with open(TITLES_CSV_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Title"])
        for title in titles:
            writer.writerow([title])
    print(f"Book titles have been extracted to {TITLES_CSV_FILE}.")

# Extract book years to a CSV file
def extract_years(books):
    years = [details['year'] for details in books.values()]
    with open(YEARS_CSV_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Year"])
        for year in years:
            writer.writerow([year])
    print(f"Book years have been extracted to {YEARS_CSV_FILE}.")

# Search for a book by title
def search_book(books):
    search_title = input("Enter the title of the book you are searching for: ")
    book_found = False

    for book_id, details in books.items():
        if details.get('title', '').lower() == search_title.lower():


            print(f"Title: {details.get('title', 'Unknown Title')}")
            print(f"Author: {details.get('author', 'Unknown Author')}")
            print(f"Genre: {details.get('genre', 'Unknown Genre')}")
            print(f"Publication Year: {details.get('year', 'Unknown Year')}")
            print(f"Price: ${details.get('price', 0.0):.2f}")
            book_found = True
            break

            

    if not book_found:
        print("Book not found.")

# Sort books by title
def sort_books(books):
    sorted_books = sorted(books.items(), key=lambda x: x[1].get('title', '').lower())
    if not sorted_books:
        print("No books available.")
        return

    for book_id, details in sorted_books:
        title = details.get('title', 'Unknown Title')
        print(f"{book_id}. Title: {title}")

# Find the oldest book
def find_oldest_book(books):
    oldest_book = None
    oldest_year = float('inf')

    for book_id, details in books.items():
        year = details.get('year', float('inf'))
        if year < oldest_year:
            oldest_book = details
            oldest_year = year

    if oldest_book:
        print(f"Title: {oldest_book.get('title', 'Unknown Title')}")
        print(f"Author: {oldest_book.get('author', 'Unknown Author')}")
        print(f"Genre: {oldest_book.get('genre', 'Unknown Genre')}")
        print(f"Publication Year: {oldest_book.get('year', 'Unknown Year')}")
        print(f"Price: ${oldest_book.get('price', 0.0):.2f}")
    else:
        print("No books available.")

# Find the newest book
def find_newest_book(books):
    newest_book = None
    newest_year = 0

    for book_id, details in books.items():
        year = details.get('year', 0)
        if year > newest_year:
            newest_book = details
            newest_year = year

    if newest_book:
        print(f"Title: {newest_book['title']}")
        print(f"Author: {newest_book['author']}")
        print(f"Genre: {newest_book['genre']}")
        print(f"Publication Year: {newest_book['year']}")
       # print(f"Price: ${newest_book['price']:.2f}")
        print(f"Price: £{newest_book.get('price', 0.0):.2f}")
    else:
        print("No books available.")

# Count titles by author
def count_titles_by_author(books):
    author_name = input("Enter the author's name: ")
    title_count = 0

    for details in books.values():
        if details.get('author', '').lower() == author_name.lower():
            title_count += 1

    print(f"Number of titles by {author_name}: {title_count}")

# def print_colored_text():
#     text = r"""    
#  ______                _     ___  ___                                                           _     _____              _                    
# | ___ \              | |    |  \/  |                                                          | |   /  ___|            | |                   
# | |_/ /  ___    ___  | | __ | .  . |  __ _  _ __    __ _   __ _   ___  _ __ ___    ___  _ __  | |_  \ `--.  _   _  ___ | |_   ___  _ __ ___  
# | ___ \ / _ \  / _ \ | |/ / | |\/| | / _` || '_ \  / _` | / _` | / _ \| '_ ` _ \  / _ \| '_ \ | __|  `--. \| | | |/ __|| __| / _ \| '_ ` _ \ 
# | |_/ /| (_) || (_) ||   <  | |  | || (_| || | | || (_| || (_| ||  __/| | | | | ||  __/| | | || |_  /\__/ /| |_| |\__ \| |_ |  __/| | | | | |
# \____/  \___/  \___/ |_|\_\ \_|  |_/ \__,_||_| |_| \__,_| \__, | \___||_| |_| |_| \___||_| |_| \__| \____/  \__, ||___/ \__| \___||_| |_| |_|
#                                                            __/ |                                             __/ |                           
#                                                           |___/                                             |___/  
#     """

#     # ANSI escape sequences for colors
#     CYAN = '\033[96m'
#     RESET = '\033[0m'
#     BOLD = '\033[1m'

#     # Print colored text
#     print(f"{CYAN}{BOLD}{text}{RESET}")



# Main menu
def main():
    books = load_books()

    while True:
        
        #print_colored_text()
        print("====================================================================")
        print("Book\tManagement\tSystem")
        print("====================================================================")
        print("1. Add Book")
        print("2. View Books")
        print("3. Extract Titles to CSV")
        print("4. Extract Years to CSV")
        print("5. Search Book")
        print("6. Sort Books by Title")
        print("7. Find Oldest Book")
        print("8. Find Newest Book")
        print("9. Count Titles by Author")
        print("10. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book(books)
        elif choice == '2':
            view_books(books)
        elif choice == '3':
            extract_titles(books)
        elif choice == '4':
            extract_years(books)
        elif choice == '5':
            search_book(books)
        elif choice == '6':
            sort_books(books)
        elif choice == '7':
            find_oldest_book(books)
        elif choice == '8':
            find_newest_book(books)
        elif choice == '9':
            count_titles_by_author(books)
        elif choice == '10':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
