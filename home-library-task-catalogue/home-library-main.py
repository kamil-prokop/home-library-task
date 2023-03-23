import sqlite3

#creating 1 database with 3 tables: books, authors, library_status
connection = sqlite3.connect("home-library.db")
cursor = connection.cursor()

#table concerning books: title
sql_books = """
CREATE TABLE IF NOT EXISTS table_books(
    id INTEGER PRIMARY KEY,
    book_title TEXT NOT NULL
);
"""

#table concerning authors: name, surname
sql_authors = """
CREATE TABLE IF NOT EXISTS table_authors(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    surname TEXT NOT NULL
);
"""

#table library as combo(many2many): books, name, surname, availability (2 statuses: YER or NO)  
sql_library = """
CREATE TABLE IF NOT EXISTS table_library(
    books_title TEXT NOT NULL,
    authors_name TEXT NOT NULL,
    authors_surname TEXT NOT NULL,
    availability VARCHAR(3) NOT NULL,
    FOREIGN KEY (books_title) REFERENCES table_books (book_title),
    FOREIGN KEY (authors_name) REFERENCES table_authors (name),
    FOREIGN KEY (authors_surname) REFERENCES table_authors (surname)
);
"""

cursor.execute(sql_books)
connection.commit()

cursor.execute(sql_authors)
connection.commit()

cursor.execute(sql_library)
connection.commit()

connection.close()