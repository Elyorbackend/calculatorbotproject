import sqlite3
db=sqlite3.connect('data.db')
cur=db.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS amallar(id TEXT,son TEXT,amal TEXT,son_2 TEXT,belgi TEXT)""")
db.commit()
db.close()
def add_user(id):
    db = sqlite3.connect('data.db')
    cur = db.cursor()
    amallar = cur.execute(f"""SELECT * FROM amallar """).fetchall()
    cur.execute(f"""INSERT INTO amallar VALUES ("{id}",'0','0','0','0')""")

    db.commit()
    db.close()
def get_son(id):
    db = sqlite3.connect('data.db')
    cur = db.cursor()
    amallar = cur.execute(f"""SELECT * FROM amallar""").fetchall()
    for i in amallar:
        if i[0] == str(id):
            if i[1]=='0':
                return i[0]

            elif i[2]=='0':
                return i[1]
            elif i[3]=='0':
                return [i[1],i[2]]
            else :
                return [i[1],i[2],i[3]]
    db.commit()
    db.close()
def change_belgi(id):
    db = sqlite3.connect('data.db')
    cur = db.cursor()
    amallar = cur.execute("""SELECT * FROM amallar """).fetchall()
    for i in amallar:
        if i[0] == str(id):
            cur.execute(F"""UPDATE amallar SET belgi='1' WHERE id='{id}' """)
    db.commit()
    db.close()


def change_son(id, n):
    db = sqlite3.connect('data.db')
    cur = db.cursor()
    amallar = cur.execute(F"""SELECT * FROM amallar """).fetchall()
    for i in amallar:
        if i[0] == str(id):
            if i[4] == '0':
                son = int(f"{i[1]}{n}")
                cur.execute(F"""Update amallar SET son='{son}' WHERE id='{id}' """)
            else:
                son1 = int(f"{i[3]}{n}")
                cur.execute(F"""Update amallar SET son_2='{son1}' WHERE id='{id}' """)

    db.commit()
    db.close()
def change_amal(id,amal):
    db = sqlite3.connect('data.db')
    cur = db.cursor()
    amallar=cur.execute(f"""SELECT * FROM amallar""").fetchall()
    for i in amallar:
        if i[0] == str(id):


            cur.execute(f"""UPDATE amallar SET amal='{amal}' WHERE id='{id}' """)
    db.commit()
    db.close()

def GetRes(id):
    db = sqlite3.connect('data.db')
    cur = db.cursor()
    amallar = cur.execute("""SELECT * FROM amallar """).fetchall()
    for i in amallar:
        if i[0] == str(id):
            if i[2]=='0':
                db.commit()
                db.close()
                return i[1]

            else:
                cur.execute(F"""UPDATE amallar SET son_2='eval(f"{i[1]} {i[2]} {i[3]}")' , amal='0',son_2='0',belgi='0' WHERE id ='{id}' """)
                db.commit()
                db.close()
                if i[2]=='*' or i[2]=="/" and i[3]=="0":
                    return eval(f"{i[1]} {i[2]} 1")
                else:
                    return eval(f"{i[1]} {i[2]} {i[3]}")
def clear(id):
    db = sqlite3.connect('data.db')
    cur = db.cursor()
    amallar=cur.execute("""SELECT * FROM amallar """).fetchall()
    for i in amallar:
        if i[0] == str(id):
            cur.execute(F"""UPDATE amallar SET son='0',amal='0',son_2='0',belgi='0' WHERE id ='{id}' """)
            db.commit()
            db.close()
            return 'Tozalandi'













