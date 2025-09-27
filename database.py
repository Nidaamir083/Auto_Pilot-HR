import sqlite3
import os

DB_PATH = "data/employees.db"

def init_db():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT, last_name TEXT,
        email TEXT UNIQUE, phone TEXT,
        department TEXT, position TEXT,
        date_of_hire TEXT, salary REAL,
        address TEXT
    )""")
    c.execute("""CREATE TABLE IF NOT EXISTS leaves (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        emp_id INTEGER,
        start_date TEXT,
        end_date TEXT,
        reason TEXT,
        status TEXT DEFAULT 'Pending',
        FOREIGN KEY(emp_id) REFERENCES employees(id)
    )""")
    conn.commit()
    conn.close()

def get_employees():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM employees")
    rows = c.fetchall()
    conn.close()
    return rows

def add_employee(emp):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""INSERT INTO employees 
        (first_name,last_name,email,phone,department,position,date_of_hire,salary,address)
        VALUES (?,?,?,?,?,?,?,?,?)""", emp)
    conn.commit()
    conn.close()

def apply_leave(emp_id, start_date, end_date, reason):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO leaves (emp_id,start_date,end_date,reason) VALUES (?,?,?,?)",
              (emp_id, start_date, end_date, reason))
    conn.commit()
    conn.close()

def get_leaves():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""SELECT leaves.id, employees.first_name||' '||employees.last_name, 
                        leaves.start_date, leaves.end_date, leaves.reason, leaves.status
                 FROM leaves JOIN employees ON leaves.emp_id = employees.id""")
    rows = c.fetchall()
    conn.close()
    return rows

def update_leave(leave_id, status):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE leaves SET status=? WHERE id=?", (status, leave_id))
    conn.commit()
    conn.close()
