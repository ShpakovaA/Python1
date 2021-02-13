import sqlite3
conn=sqlite3.connect('Phonebook.db')
c=conn.cursor()
c.execute("""CREATE TABLE contact (contact_id INTEGER PRIMARY KEY, Name TEXT, Surname TEXT, Phone_number INTEGER)""")
c.execute("INSERT INTO contact VALUES (1, 'John', 'Adams', 75678986)")
conn.commit()
conn.close()
