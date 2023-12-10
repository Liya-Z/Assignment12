import sqlite3
import pandas as pd

connection = sqlite3.connect('books.db')
pd.options.display.max_columns = 10
author_data = pd.read_sql('SELECT * FROM authors', connection, index_col=['id'])
title_data = pd.read_sql('SELECT * FROM titles', connection)
df = pd.read_sql('SELECT * FROM author_ISBN', connection)
author_data2 = pd.read_sql('SELECT first, last FROM authors', connection)
copyright_data = pd.read_sql("""SELECT title, edition, copyright
                FROM titles
                WHERE copyright > '2016'""", connection)

author_id = pd.read_sql("""SELECT id, first, last
                FROM authors
                WHERE last LIKE 'D%'""",
                connection, index_col=['id'])

author_id2 = pd.read_sql("""SELECT id, first, last
                FROM authors
                WHERE first LIKE '_b%'""",
connection, index_col=['id'])

title_ordered = pd.read_sql('SELECT title FROM titles ORDER BY title ASC',
            connection)

sort_columns = pd.read_sql("""SELECT id, first, last
                FROM authors
                ORDER BY last, first""",
connection, index_col=['id'])

ascending_order = pd.read_sql("""SELECT id, first, last
                FROM authors
                ORDER BY last DESC, first ASC""",
                connection, index_col=['id'])


select_and_order_by_title = pd.read_sql("""SELECT isbn,
                title, edition, copyright
                FROM titles
                WHERE title LIKE '%How to Program'
                ORDER BY title""", connection)
inner_join_isbn = pd.read_sql("""SELECT first, last, isbn
                FROM authors
                INNER JOIN author_ISBN
                ON authors.id = author_ISBN.id
                ORDER BY last, first""", connection).head()

cursor = connection.cursor()
cursor = cursor.execute("""INSERT INTO authors (first, last)
                            VALUES ('Sue', 'Red')""")


author_info = pd.read_sql('SELECT id, first, last FROM authors',
connection, index_col=['id'])


cursor = cursor.execute("""UPDATE authors SET last='Black'
                            WHERE last='Red' AND first='Sue'""")
row_num = cursor.rowcount


updated_info = pd.read_sql('SELECT id, first, last FROM authors', connection, index_col=['id'])

cursor = cursor.execute('DELETE FROM authors WHERE id=6')
row_num2 = cursor.rowcount
delete_updated_info = pd.read_sql('SELECT id, first, last FROM authors',
 connection, index_col=['id'])

df.head()
print(title_data, "\n", author_data, "\n", author_data2, " \n", copyright_data, "\n",
     author_id, "\n", author_id2, "\n", title_ordered, "\n", sort_columns, "\n",
      ascending_order, "\n", select_and_order_by_title, "\n", inner_join_isbn, "\n", author_info, "\n", row_num, "\n", updated_info, "\n",
     row_num2, "\n", delete_updated_info)

