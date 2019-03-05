import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute("drop table if exists Counts")
cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")


name = input("Enter a file name: ")
if len(name)<1: data=open("mbox-short.txt")
else: data = open(name)

pair = dict()
for line in data:
    if not line.startswith('From:'): continue
    else:
        emailfull = line.split('@')
        org = emailfull[1].rstrip()
        pair[org]=pair.get(org,0)+1

for key in pair:
    cur.execute('INSERT INTO Counts (org, count) VALUES (?,?)',(key,pair[key]))



res_table = cur.execute('SELECT * FROM Counts ORDER BY count DESC')

for item in res_table:
    print (item[0], item[1])

conn.commit()

conn.close()