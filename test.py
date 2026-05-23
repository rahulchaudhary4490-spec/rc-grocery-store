import psycopg2

conn = psycopg2.connect('postgresql://todo_database_1sjn_user:650X0ZksXFXbBrBFkysGz1UdOrrkdoC5@dpg-d83c8qbtqb8s73diu2b0-a.oregon-postgres.render.com/todo_database_1sjn')
cur = conn.cursor()
cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
for t in cur:
    print(t)