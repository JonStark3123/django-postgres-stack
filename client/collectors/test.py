#!/usr/bin/env python3
import subprocess, psycopg2, sys

if __name__ == '__main__':
    DBNAME = 'TestDB'
    DBUSER = 'postgres'
    DBPASSWORD='password'
    DBHOST='127.0.0.1'
    DBPOT='5432'
    table_name ='testdb'

    # print('dbname={} user={}'.format(DBNAME, DBUSER))
    # sys.exit()

    # delete the pgbench DB if it already exists
    # input("About to drop the pgbench database! Press 'Ctrl-C' to cancel or 'Return' to continue.")
    # subprocess.call(['dropdb', 'pgbench'])
    # create the test database
    # subprocess.call(['createdb', 'pgbench'])
    # initialize the test database with some stock pgbench options
    # subprocess.call(['pgbench', '-i', '-s', '10', DBNAME])
    # psycopg2.connect(database="testdb", user="postgres", password="cohondob", host="127.0.0.1", port="5432")
    try:
        conn = psycopg2.connect('dbname={} user={} password={} host={} port={}'.format(DBNAME, DBUSER,DBPASSWORD,DBHOST,DBPOT))
    except Exception as e:
        print("[!] ", e)
    else:
        with conn:
            with conn.cursor() as curs:
                curs.execute('''CREATE TABLE ''' + table_name +
                      ''' (file_path TEXT PRIMARY KEY NOT NULL, 
                      file_hash TEXT, 
                      check_some TEXT,
                      file_inode TEXT NOT NULL, 
                      file_permission TEXT NOT NULL,
                      file_uid TEXT NOT NULL,
                      file_gid TEXT NOT NULL, 
                      file_reference TEXT NOT NULL, 
                      file_table TEXT NOT NULL);''')
    finally:
            conn.close()