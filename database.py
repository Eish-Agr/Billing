import cx_Oracle
try:
    conn = cx_Oracle.connect('system/2580@//localhost:1521/xepdb1')
except Exception as err:
    print("Error while creating the connection", err)
else:
    print(conn.version)
    try:
        cur = conn.cursor()
        sql_insert="""INSERT INTO BILLING 
         VALUES (to_date('01-07-2024','DD-MM-YYYY'),'FGH','RING',18,72500,10,72000) """
        cur.execute(sql_insert)
    except Exception as err:
        print("Error while inserting the data", err)
    else:
        print("Insert Complete.")
        conn.commit()
finally:
    cur.close()
    conn.close()






print('Table Created.')