import sqlite3

con = sqlite3.connect("rms.db")
cur = con.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables found:", cur.fetchall())
con.close()
