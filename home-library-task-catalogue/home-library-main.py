import sqlite3

#creating 1 database with 3 tables: books, authors, library_status
db_file = "home-library.db"
connection = sqlite3.connect(db_file)
connection.execute('''PRAGMA foreign_keys=ON''')
cursor = connection.cursor()

#table concerning books: title
sql_books = """
CREATE TABLE IF NOT EXISTS table_books(
    book_title TEXT PRIMARY KEY NOT NULL
);
"""

#table concerning authors: name, surname
sql_authors = """
CREATE TABLE IF NOT EXISTS table_authors(
    name TEXT PRIMARY KEY NOT NULL
);
"""

#table library as combo(many2many): books, name, surname, availability (2 statuses: YER or NO)  
sql_library = """
CREATE TABLE IF NOT EXISTS table_library(
    books_title TEXT NOT NULL REFERENCES table_books (book_title),
    authors_name TEXT NOT NULL REFERENCES table_authors (name),
    availability VARCHAR(3) NOT NULL
);
"""

cursor.execute(sql_books)
connection.commit()

cursor.execute(sql_authors)
connection.commit()

cursor.execute(sql_library)
connection.commit()

#inserting data into tables

cursor.execute('''INSERT OR IGNORE INTO table_books (book_title) VALUES ("Propaganda")''')
cursor.execute('''INSERT OR IGNORE INTO table_books (book_title) VALUES ("Inżynieria finansowa")''')
cursor.execute('''INSERT OR IGNORE INTO table_books (book_title) VALUES ("Działa Nawarony")''')
cursor.execute('''INSERT OR IGNORE INTO table_books (book_title) VALUES ("Tylko dla orłów")''')

connection.commit()


cursor.execute('''INSERT OR IGNORE INTO table_authors (name) VALUES ("Edward Bernays")''')
cursor.execute('''INSERT OR IGNORE INTO table_authors (name) VALUES ("Rafał Weron")''')
cursor.execute('''INSERT OR IGNORE INTO table_authors (name) VALUES ("Alistair MacLean")''')

connection.commit()


cursor.execute('''INSERT OR IGNORE INTO table_library (books_title, authors_name, availability) VALUES ("Propaganda", "Edward Bernays", "NO")''')
cursor.execute('''INSERT OR IGNORE INTO table_library (books_title, authors_name, availability) VALUES ("Inżynieria finansowa", "Rafał Weron", "YES")''')
cursor.execute('''INSERT OR IGNORE INTO table_library (books_title, authors_name, availability) VALUES ("Działa Nawarony", "Alistair MacLean", "NO")''')
cursor.execute('''INSERT OR IGNORE INTO table_library (books_title, authors_name, availability) VALUES ("Tylko dla orłów", "Alistair MacLean", "YES")''')

connection.commit()


connection = sqlite3.connect(db_file)
cursor = connection.cursor()
sql_select_books = f"SELECT * FROM table_books"
sql_select_authors = f"SELECT * FROM table_authors"
sql_select_library = f"SELECT * FROM table_library"
cursor.execute(sql_select_library)
results = cursor.fetchall()
print(results)
connection.close()
