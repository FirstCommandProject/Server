import mysql.connector


# Функция, которая выполняет sql запрос select к таблице Questions по столбцу id

def select_table_questions_id(id):
    mycursor = database.cursor()
    sql = f"SELECT * FROM Questions WHERE id = {id}"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        return None
    else:
        return myresult


# Функция, которая выполняет sql запрос select к таблице Questions по столбцу text


def select_table_questions_text(text):
    mycursor = database.cursor()
    sql = f"SELECT * FROM Questions WHERE text = {text}"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        return None
    else:
        return myresult


# Функция, которая выполняет sql запрос select к таблице Questions по столбцу tags


def select_table_questions_tags(tags):
    mycursor = database.cursor()
    sql = f"SELECT * FROM Questions WHERE JSON_CONTAINS(tags, '[{tags}]')"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        return None
    else:
        return myresult


if __name__ == '__main__':
    database = mysql.connector.connect(
        host="localhost",
        user="Dima",
        password="Zerg123456789ertyama_",
        database="expertsystem"
    )
