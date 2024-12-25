import pyodbc
teslead_db = None
def local_db():
    global teslead_db
    teslead_X = "DRIVER={MySQL ODBC 9.0 ANSI Driver};Server=localhost;Port=3306;Database=qnq;Uid=root;Password=;OPTION=3;"
    conn = pyodbc.connect(teslead_X)
    try:
        teslead_db = conn.cursor()
    except Exception as e:
        print(f"Database connection error: {e}")
        local_db()
local_db()

ip_address = teslead_db.execute("select ip_address from master_ip_address;").fetchone()[0]
print(ip_address)