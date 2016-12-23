import sqlite3
con  = sqlite3.connect('db1.db')
cur = con.cursor()
create_table="create table persons(name vatrchar(50), password varchar(50), cell varchar(12), email varchar(50))"
try:
    cur.execute(create_table)
except Exception as err:
	print err
finally:
     con.commit()
     cur.close()
     con.close()