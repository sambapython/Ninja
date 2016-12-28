
import sqlite3
import pdb
import pandas as pd


def get_cur():
    con = sqlite3.connect('db1.db')
    cur = con.cursor()
    return cur, con


def close_cur(cur, con):
    cur.close()
    con.close()


def check_user(username, password):
    res=""
    query = "select * from persons where name='{0}' and password='{1}'"\
        .format(username, password)
    try:
        cur, con = get_cur()
        #data = pd.read_sql(query,con)
        #pdb.set_trace()
        cur.execute(query)
        res = cur.fetchone() 
    except Exception as err:
        res=False
    finally:
        con.commit()
        close_cur(cur, con)

    return res




def insert(data):
    """
     params-mandatory:
            data type: dict
     params-defaultL

     return : True if inserted successfully otherwise False
     desc: inserts the dictionary details into database
    """
    res=""
    query = "insert into persons values('{0}','{1}','{2}','{3}')".format(
            data.get('name'),
            data.get('password'),
            data.get('cell'),
            data.get('email')
    )
    try:
        cur, con = get_cur()
        cur.execute(query)
        res= "Successfully inserted"
    except Exception as err:
        res = err
    finally:
        con.commit()
        close_cur(cur, con)

    return res

check_user('name1','pwd1')  
