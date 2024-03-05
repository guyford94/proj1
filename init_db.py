import sqlite3

connection = sqlite3.connect('users.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users (Name, Email) VALUES (?, ?)",
            ('Guy Ford', 'guy@guy.com')
            )

cur.execute("INSERT INTO users (Name, Email) VALUES (?, ?)",
            ('Noa Ford', 'Noa@guy.com')
            )



def add_user(cur , name , email):
    cur.execute("INSERT INTO users (Name, Email) VALUES (?, ?)",
            (name, email)
            )

connection.commit()
connection.close()