import mysql.connector

def select_questions_by_tag(tag):
    data_base_cursor = database.cursor()
    query = f"SELECT * FROM Questions WHERE JSON_CONTAINS(tags, '[\"{tag}\"]', \"$\") ORDER BY RAND LIMIT 1"
    data_base_cursor.execute(query)


def insert(login, lastlogintime):
    mycursor = database.cursor()
    sql = f"INSERT INTO data (login, lastLoginTime) VALUES ('{login}', '{lastlogintime}')"
    mycursor.execute(sql)
    database.commit()


def upsert(nameofcolumn, strokanavhod, id):
    mycursor = database.cursor()
    if nameofcolumn == "login":
        sql = f"UPDATE data SET login = '{strokanavhod}' WHERE id = '{id}'"
        mycursor.execute(sql)
        database.commit()
    else:
        sql = f"UPDATE data SET lastLoginTime = '{strokanavhod}' WHERE id = '{id}'"
        mycursor.execute(sql)
        database.commit()


def selectbyid(id):
    mycursor = database.cursor()
    sql = f"SELECT login FROM data WHERE id = '{id}'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)


def selectbyiddata(id):
    mycursor = database.cursor()
    sql = f"SELECT lastLoginTime FROM data WHERE id = '{id}'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)


def selectallbyid(id):
    mycursor = database.cursor()
    sql = f"SELECT * FROM data WHERE id = '{id}'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)


def sort(basestringofsort, keyofsort):
    mycursor = database.cursor()
    sql = f"SELECT * FROM data ORDER BY '{basestringofsort}' '{keyofsort}'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)


if __name__ == '__main__':
    database = mysql.connector.connect(
        host="localhost",
        user="Dima",
        password="Zerg123456789ertyama_",
        database="expertsystem"
    )
    databaseQuery = input()
    if databaseQuery == "INSERT":
        log, lastlogtime = input(), input()
        insert(log, lastlogtime)
    elif databaseQuery == "UPSERT":
        id = int(input())
        nameofcolumn, strokanavhod = input(), input()
        upsert(nameofcolumn, strokanavhod, id)
    elif databaseQuery == "SELECT BY ID login":
        id = int(input())
        selectbyid(id)
    elif databaseQuery == "SELECT BY ID data":
        id = int(input())
        selectbyiddata(id)
    elif databaseQuery == "SELECT ALL BY ID":
        id = int(input())
        selectallbyid(id)
    elif databaseQuery == "SORTIROVKA":
        basestringofsort, keyofsort = input(), input()
        sort(basestringofsort, keyofsort)
