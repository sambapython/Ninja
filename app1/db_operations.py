
import sqlite3
def get_cur():
	con = sqlite3.connect('db1.db')
	cur=con.cursor()
	return cur,con
def close_cur(cur,con):
	cur.close()
	con.close()

def insert(data):
	"""
	 params-mandatory: 
		data type: dict
	 params-defaultL

	 return : True if inserted successfully otherwise False
	 desc: inserts the dictionary details into database
	"""
	query = "insert into persons values('{0}','{1}','{2}','{3}')".format(
		data.get('name'),
		data.get('password'),
		data.get('cell'),
		data.get('email')
		)
	try:
		cur,con = get_cur()
		cur.execute(query)

	except Exception as err:
		return err
	finally:
		con.commit()
		close_cur(cur,con)
	return "Successfully inserted"


