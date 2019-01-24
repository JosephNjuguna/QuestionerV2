"""" Main connection to the postgres database """
import psycopg2, psycopg2.extras

from app.api.v2.models.database import create_tables, create_admin, drop_existing_tables

class DatabaseConnection:

    def __init__(self, db_url):
        """ initialize the class instance to take a database url as a parameter"""
        try:
            global conn, cur
            conn = psycopg2.connect(db_url)
            cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        except Exception as error:
            print('Unable to connect to database:', error)

    def create_tables_and_admin(self):
        """ creates all tables """
        all_tables_to_create = create_tables()
        for query in all_tables_to_create:
            cur.execute(query)
            conn.commit()
        create_admin(conn)

    def drop_all_tables(self):
        """ Deletes all tables in the app """
        tables_to_drop = drop_existing_tables()
        for query in tables_to_drop:
            cur.execute(query)
            conn.commit

    def fetch_single_data_row(self, query):
        """ retreives a single row of data from a table """
        cur.execute(query)
        fetchedRow = cur.fetchone()
        return fetchedRow
        cur.close()


    def save_incoming_data_or_updates(self, query):
        """ saves data passed as a query to the stated table """
        cur.execute(query)
        result_id = cur.fetchone()
        conn.commit()
        return result_id
        cur.close()


    def fetch_all_tables_rows(self, query):
        """ fetches all rows of data store """
        cur.execute(query)
        all_data_rows = cur.fetchall()
        return all_data_rows
        cur.close()
