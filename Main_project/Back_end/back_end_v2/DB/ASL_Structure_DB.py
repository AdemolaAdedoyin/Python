import sqlite3

database = r"C:\Users\Ademola Adedoyin\Downloads\MDX Stuff\Thesis\Main_project\Back_end\Thesis_FYP.db"
names = ""


def createDB():
    db_conn = sqlite3.connect(database, check_same_thread=False)
    print("Databases connected")
    try:
        db_conn.execute("DROP TABLE IF EXISTS Image_Table")
        db_conn.commit()
        db_conn.execute("CREATE TABLE Image_Table(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Word TEXT NOT NULL, "
                        "Part_of_speech TEXT NOT NULL, URL TEXT NOT NULL);")
        db_conn.commit()
        print("table created")
    except sqlite3.OperationalError:
        print("already exit")
    db_conn.close()
    print("Database closed")


# createDB()

def create_table(word, POS, URL):
    db_conn = sqlite3.connect(database, check_same_thread=False)
    new_cursor = db_conn.cursor()
    try:
        new_cursor.execute("INSERT INTO Image_Table (Word,Part_of_speech,URL) VALUES (?,?,?)",
                           (word, POS, URL))
        all_all = new_cursor.fetchall()
    except sqlite3.OperationalError:
        all_all = "Error"
    db_conn.commit()
    new_cursor.close()
    db_conn.close()
    return all_all


# create_table()
def getAll():
    db_conn = sqlite3.connect(database, check_same_thread=False)
    # to return a single row data
    # db_conn.row_factory = sqlite3.Row
    new_cursor = db_conn.cursor()
    global names
    # names = list(map(lambda x: x[0], new_cursor.description))
    try:
        new_cursor.execute("SELECT * FROM ASL_Universal_Structure")
        all_all = new_cursor.fetchall()
    except sqlite3.OperationalError as e:
        all_all = e
    new_cursor.close()
    db_conn.close()
    return all_all

def get_one_where(pos):
    db_conn = sqlite3.connect(database, check_same_thread=False)
    # to return a single row data
    db_conn.row_factory = sqlite3.Row
    new_cursor = db_conn.cursor()
    # print(id)
    try:
        # new_cursor.execute('''SELECT * FROM English_table WHERE Sentence=?''', sentence)
        new_cursor.execute("""SELECT * FROM ASL_Universal_Structure WHERE ENGLISH="{pos}" """.format(pos=pos))
        all_all = new_cursor.fetchone()
    except sqlite3.DatabaseError and sqlite3.OperationalError and sqlite3.DataError and sqlite3.Error as e:
        all_all = e
    if all_all is None or all_all == "Error":
        new_cursor.close()
        db_conn.close()
        return all_all
    else:
        # all_all = all_all['POS_tag']
        new_cursor.close()
        db_conn.close()
        return all_all

def get_one_where_id(uid):
    db_conn = sqlite3.connect(database, check_same_thread=False)
    # to return a single row data
    db_conn.row_factory = sqlite3.Row
    new_cursor = db_conn.cursor()
    # print(id)
    try:
        # new_cursor.execute('''SELECT * FROM English_table WHERE Sentence=?''', sentence)
        new_cursor.execute("""SELECT * FROM ASL_Universal_Structure WHERE ID="{uid}" """.format(uid=uid))
        all_all = new_cursor.fetchone()
    except sqlite3.DatabaseError and sqlite3.OperationalError and sqlite3.DataError and sqlite3.Error as e:
        all_all = e
    if all_all is None or all_all == "Error":
        new_cursor.close()
        db_conn.close()
        return all_all
    else:
        # all_all = all_all['POS_tag']
        new_cursor.close()
        db_conn.close()
        return all_all


# print(get_one_where("['ADV', 'VERB', 'PRON', 'VERB', '.']")['ASL'])

def row_names():
    db_conn = sqlite3.connect(database, check_same_thread=False)
    new_cursor = db_conn.cursor()
    new_cursor.execute("PRAGMA TABLE_INFO(ASL_Universal_Structure)")
    rowNames = [nameTuple[1] for nameTuple in new_cursor.fetchall()]
    new_cursor.close()
    db_conn.close()
    return rowNames


def update_one_where(where_to_update, what_to_update):
    db_conn = sqlite3.connect(database, check_same_thread=False)
    new_cursor = db_conn.cursor()
    try:
        wordwewe = "word"
        new_cursor.execute('''UPDATE ASL_Universal_Structure SET ? = ? WHERE ID=2''', (wordwewe, what_to_update,))
        # new_cursor.execute("UPDATE Image_Table SET Word = 'Help' WHERE ID=2")
        # new_cursor.execute("UPDATE Image_Table SET {wto} = {wtu} WHERE ID=1"
        #                    .format(wto=where_to_update, wtu=what_to_update))
        db_conn.commit()
        all_all = new_cursor.fetchone()
    except sqlite3.OperationalError as e:
        all_all = e
    new_cursor.close()
    db_conn.close()
    return all_all


# update_one_where("Word","Push")

def delete_one_where(Table_name, location, uid):
    db_conn = sqlite3.connect(database, check_same_thread=False)
    new_cursor = db_conn.cursor()
    try:
        new_cursor.execute("DELETE FROM {} WHERE {}={}".format(Table_name, location, uid))
        db_conn.commit()
        all_all = new_cursor.fetchone()
    except sqlite3.OperationalError as e:
        all_all = e
    new_cursor.close()
    db_conn.close()
    return all_all