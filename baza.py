import mysql.connector

# Uzupełnij dane!
mydb = mysql.connector.connect(
    host="",
    user="",
    passwd="",
    database=""
)

mycursor = mydb.cursor()

def bazacl(output):
    x = output
    t = []
    for i in x:
        z = str(i)
        z = z.replace("(", "")
        z = z.replace(")", "")
        z = z.replace(",", "")
        z = z.replace("'", "")
        t.append(z)
    t = t[0].split(sep=" ")
    return t

def pol(id):
    try:
        sql = "SELECT * FROM XO WHERE id ='" + id + "';"
        mycursor.execute(sql)
        out = mycursor.fetchall()
        out = bazacl(out)
        if out[10] == '0':
            sql = "UPDATE XO SET gracz1 = 1 WHERE id = '" + id + "';"
            mycursor.execute(sql)
            mydb.commit()
            out[10] = '1'
            gracz = 1
            return out, gracz
        elif out[11] == '0':
            sql = "UPDATE XO SET gracz2 = 1 WHERE id = '" + id + "';"
            mycursor.execute(sql)
            mydb.commit()
            out[11] = '1'
            gracz = 2
            return out, gracz
        else:
            return None, None
    except:
        sql = "INSERT INTO XO (id, x1, x2, x3, x4, x5, x6, x7, x8, x9, gracz1, gracz2, teraz) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (id, "A", "A", "A", "A", "A", "A", "A", "A", "A", 1, 0, "X")
        mycursor.execute(sql, val)
        mydb.commit()
        sql = "SELECT * FROM XO WHERE id ='" + id + "';"
        mycursor.execute(sql)
        out = mycursor.fetchall()
        out = bazacl(out)
        return out, 1

def rozlacz(id, gracz):
    if gracz == 1:
        sql = "UPDATE XO SET gracz1 = 0 WHERE id = '" + id + "';"
        mycursor.execute(sql)
        mydb.commit()
    elif gracz == 2:
        sql = "UPDATE XO SET gracz2 = 0 WHERE id = '" + id + "';"
        mycursor.execute(sql)
        mydb.commit()

def pobierz(id):
    mydbb = mysql.connector.connect(
        host="51.68.137.108",
        user="pythondb",
        passwd="pythondb_pass",
        database="pythondb"
    )
    mycursorb = mydbb.cursor()

    sql = "SELECT * FROM XO WHERE id ='" + id + "';"
    mycursorb.execute(sql)
    out = mycursorb.fetchall()
    out = bazacl(out)
    return out

def updt(id, nr, txt, kolej):
    sql = "UPDATE XO SET "+nr+" = '"+txt+"' WHERE id ='"+ id +"';"
    mycursor.execute(sql)
    mydb.commit()
    sql = "UPDATE XO SET teraz = '"+kolej+"' WHERE id ='"+ id +"';"
    mycursor.execute(sql)
    mydb.commit()

def usun(id):
    sql = "DELETE FROM XO WHERE id = '"+ id +"';"
    mycursor.execute(sql)
    mydb.commit()