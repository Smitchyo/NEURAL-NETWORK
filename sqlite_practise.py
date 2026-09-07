import sqlite3
#creates a connection the tutorial database
con = sqlite3.connect('tutorial.db')

#creates a cursor to allow us to execute database queries
cur = con.cursor()

#create a databse table "movie" with columns: title, year, score
cur.execute("CREATE TABLE movie(title, year, score)")

#verify that the new table has been created by quering the "SQLITE MASTER"
res = cur.execute("SELECT name FROM sqlite_master")

#calling the res to fetch the data now
print(res.fetchone())


res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
print(res.fetchone()is None)


cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")

#commits the cur.execute into the database
con.commit()

res = cur.execute("SELECT score FROM movie")
print(res.fetchall())

data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cur.executemany("INSERT INTO movie VALUES(?,?,?)", data)
con.commit()

for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
    print(row)

con.close()
new_con = sqlite3.connect("tutorial.db")
new_cur = new_con.cursor()
res = new_cur.execute("SELECT title, year FROM movie ORDER BY score DESC")
title, year = res.fetchone()
print(f'The highest scoring Monty Python movie is {title!r}, released in {year}')

new_con.close()