import sql_7_class_0

dbRunner = sql_7_class_0.myDB('info')

rows = dbRunner.read_all()
for row in rows:
    print(row)