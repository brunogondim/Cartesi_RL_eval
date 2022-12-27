from asyncio.log import logger
import LinearAlgebraPurePython as la 
import sys
import sqlite3


con = sqlite3.connect("data.db")
cur = con.cursor()
cur.execute('SELECT * FROM medical')
r = cur.fetchall()

X = []
Y = []
for item in r:
    age = float(item[0])
    sex = 0 if item[1] == 'male' else 1
    bmi = float(item[2])
    children = float(item[3])
    smoker = 0 if item[4] == 'no' else 1
    region = item[5]
    charges = float(item[6])

    X.append([age,sex,bmi,children,smoker])
    Y.append(charges)
coefs = la.least_squares(X, Y)
la.print_matrix(coefs)
coefs_str = ' '.join(map(str,coefs))
logger.info(f"model: {coefs_str}")