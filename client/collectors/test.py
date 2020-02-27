#!/usr/bin/env python3
import glob
import os
import subprocess, psycopg2, sys
import json

from settings import SCRIPTS_DIR

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
    scriptList= []
    scriptContent = []
    scriptDir = SCRIPTS_DIR
    if os.path.exists(scriptDir):
        sqlScript = glob.glob(scriptDir + "/*.sql")

        for script in sqlScript:
            scriptObj = {}
            # fp = open(script, 'r')
            # for line in fp.readlines():
            #     scriptContent.append(line)
            # fp.close()
            # scriptObj["content"] = scriptContent
            scriptObj["scriptName"] = os.path.basename(script)
            scriptList.append(scriptObj)
        json = json.dumps(scriptList)
        print("collecting self-design script json: " + json)

    else:
        print("collecting self-design script files Error: " + scriptDir + " not exists")