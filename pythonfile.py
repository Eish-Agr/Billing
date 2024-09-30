import pandas as pd
from flask import Flask, render_template, request
import cx_Oracle, os
app=Flask(__name__, template_folder="views") 
@app.route('/')

def Dashboard():

    return render_template("Dashboard.html")

@app.route('/insert_value', methods=['post'])

def getvalue():

    date = request.form['date']
    item = request.form['item']
    name = request.form['name']
    karat = request.form['karat']
    goldprice = request.form['goldprice']
    Weight = request.form['Weight']
    Price = request.form['Price']

    try:
        conn = cx_Oracle.connect('system/2580@//localhost:1521/xepdb1')
    except Exception as err:
        print("Error while creating the connection", err)
    else:
        print(conn.version)
        try:
            cur = conn.cursor()
            sql_insert="""INSERT INTO BILLING  
            VALUES (to_date('"""+date+"""','YYYY-MM-DD'),'"""+item+"""','"""+name+"""',"""+karat+""","""+goldprice+""","""+Weight+""","""+Price+""") """
            cur.execute(sql_insert)
        except Exception as err:
            print("Error while inserting the data", err)
        else:
            print("Insert Complete.")
            conn.commit()
    finally:
        cur.close()
        conn.close()
    return render_template("submit.html")

@app.route("/get_value", methods=['post'])
def fetchvalue():
    date2 = request.form['date2']

    try:
        conn = cx_Oracle.connect('system/2580@//localhost:1521/xepdb1')
    except Exception as err:
        print("Error while creating the connection", err)
    else:
        print(conn.version)
        try:
            cur = conn.cursor()
            sql_get="""SELECT * FROM BILLING WHERE curr_date LIKE to_date('"""+date2+"""','YYYY-MM-DD') """
            cur.execute(sql_get)
            row = cur.fetchall()
            print(row)

            for index, record in enumerate(row):
                print("Index is", index, ":", record)

            df = pd.DataFrame()
            for x in row:
                df2 = pd.DataFrame(list(x)).T
                df = pd.concat([df, df2])
            df.to_html('Views/sql-data.html')

        except Exception as err:
            print("Error while fetching the data", err)
        else:
            print("fetching Complete.")
    finally:
        cur.close()
        conn.close()
    return render_template("sql-data.html")



if __name__=='__main__':
   app.run(debug=True)

