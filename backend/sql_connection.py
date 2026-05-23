import psycopg2

__cnx = None

def get_sql_connection():
    print("Opening PostgreSQL connection")
    global __cnx

    if __cnx is None or __cnx.closed:
        __cnx = psycopg2.connect(
            "postgresql://todo_database_1sjn_user:650X0ZksXFXbBrBFkysGz1UdOrrkdoC5@dpg-d83c8qbtqb8s73diu2b0-a.oregon-postgres.render.com/todo_database_1sjn"
        )
        __cnx.autocommit = False

    # If connection is in failed state, rollback to reset it
    if __cnx.status == psycopg2.extensions.STATUS_IN_TRANSACTION:
        try:
            __cnx.rollback()
        except:
            __cnx = None
            return get_sql_connection()

    return __cnx