import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """
    This function deletes all the tables, if they already exist.
    """
    print('Deleting tables')
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    This function creates staging, fact and dimensions tables designed in 'sql_queries.py'.
    """
    print('Creating tables')
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    This is the main function which creates a connection to the cluster and implements the functions defined above to create or drop tables.
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    print('Cluster is connected')
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()