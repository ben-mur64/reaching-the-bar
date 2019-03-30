import school

import sqlite3
conn = sqlite3.connect('schools.db')

def create_tables():
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS schools;")
    c.execute(open("schema.sql", "r").read())

def insert_school(school):
    c = conn.cursor()
    value = (school.name, school.full_name, school.emp_percent, school.big_law, school.small_law, school.public_service, school.clerkships, school.unemp_percent, school.debt, school.attrition, school.prestige, school.gpa, school.lsat)
    print(str(value))
    try:
        c.execute('INSERT INTO schools VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)', value)
    except Exception as e:
        print(e)

def get_all_schools():
    c = conn.cursor()
    schools = []
    for row in c.execute('SELECT * FROM schools'):
        schools.append(get_school(row))
    return schools

def get_school(row):
    name = str(row[0])
    full_name = str(row[1])
    a = float(row[2])
    b = float(row[3])
    c = float(row[4])
    d = float(row[5])
    e = float(row[6])
    f = float(row[7])
    g = float(row[8])
    h = float(row[9])
    i = float(row[10])
    j = float(row[11])
    k = float(row[12])
    return school.School(name, full_name, a, b, c, d, e, f, g, h, i, j, k)

def get_school_names():
    c = conn.cursor()
    names = []
    for row in c.execute('SELECT * FROM schools'):
        names.append(str(row[0]))
    print(str(names))
    return names