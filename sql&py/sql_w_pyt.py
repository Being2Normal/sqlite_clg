import sqlite3 as s

# connect()
con = s.connect("mydb.db")
c = con.cursor()

# create
c.execute("CREATE TABLE IF NOT EXISTS student (rno INTEGER PRIMARY KEY, name TEXT, marks INTEGER)")

# insert
c.execute("INSERT INTO student VALUES (1, 'Amit', 78)")
c.execute("INSERT INTO student VALUES (2, 'Bhavy', 15)")
c.execute("INSERT INTO student VALUES (3, 'Bhad', 95)")
c.execute("INSERT INTO student VALUES (4, 'Bhay', 45)")
c.execute("INSERT INTO student VALUES (5, 'avya', 89)")
con.commit()

# update
c.execute("UPDATE student SET marks = 90 WHERE rno = 2")
con.commit()

# delete
c.execute("DELETE FROM student WHERE rno = 1")
con.commit()

# select using fetchone()
c.execute("SELECT * FROM student WHERE rno = 2")
data1 = c.fetchone()
print("Fetch One:", data1)

# select using fetchall()
c.execute("SELECT * FROM student")
data2 = c.fetchall()
print("Fetch All:", data2)

#drop
c.execute("drop table student")

con.close()
