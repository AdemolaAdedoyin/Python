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

def create_table(word,POS,URL):
    db_conn = sqlite3.connect(database, check_same_thread=False)
    new_cursor = db_conn.cursor()
    try:
        new_cursor.execute("INSERT INTO Image_Table (Word,Part_of_speech,URL) VALUES (?,?,?)",
                           (word,POS,URL))
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
        new_cursor.execute("SELECT * FROM Image_Table")
        all_all = new_cursor.fetchall()
    except sqlite3.OperationalError as e:
        all_all = e
    new_cursor.close()
    db_conn.close()
    return all_all



def get_one_where(what,POS):
    db_conn = sqlite3.connect(database, check_same_thread=False)
    # to return a single row data
    db_conn.row_factory = sqlite3.Row
    new_cursor = db_conn.cursor()
    try:
        new_cursor.execute('''SELECT * FROM Image_Table WHERE Word=? AND Part_of_speech=?''', (what,POS))
        # new_cursor.execute("""SELECT URL FROM Image_Table WHERE {}={} """.format(wha,what))
        all_all = new_cursor.fetchone()
    except sqlite3.DatabaseError and sqlite3.OperationalError and sqlite3.DataError and sqlite3.Error:
        all_all = "Error"
    if all_all is None or all_all == "Error":
        new_cursor.close()
        db_conn.close()
        return all_all
    else:
        all_all = all_all['URL']
        new_cursor.close()
        db_conn.close()
        return all_all

# get_one_where("Moving", "Verb")


def row_names():
    db_conn = sqlite3.connect(database, check_same_thread=False)
    new_cursor = db_conn.cursor()
    new_cursor.execute("PRAGMA TABLE_INFO(Image_Table)")
    rowNames = [nameTuple[1] for nameTuple in new_cursor.fetchall()]
    new_cursor.close()
    db_conn.close()
    return rowNames


def update_one_where(where_to_update, what_to_update):
    db_conn = sqlite3.connect(database, check_same_thread=False)
    new_cursor = db_conn.cursor()
    try:
        wordwewe = "word"
        new_cursor.execute('''UPDATE Image_Table SET ? = ? WHERE ID=2''', (wordwewe, what_to_update,))
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