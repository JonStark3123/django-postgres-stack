import glob
import os.path
from settings import SCRIPTS_DIR, CUSTEMSCRIPT
from utils.logging import log
from utils.misc import run_cmd
import json


class ScriptCollector(object):
    'Collect various Linux-specific statistics (cpuinfo, mounts)'

    def __init__(self, scriptdirpath, env, dbname):
        self._dirPath = scriptdirpath
        self._env = env
        self._dbname=dbname


    def start(self):
        pass

    def stop(self):
        pass

    def result(self):
        'build the results'

        r = {'script': self._collect_scriptDir_info()}

        # r.update(self._collect_scriptDir_info())

        return r

    def _collect_sysctl(self):
        'collect kernel configuration'

        log("collecting sysctl")
        r = run_cmd(['sysctl', '-a'], env=self._env)

        return r[1]

    def _collect_scriptDir_info(self):
        scriptList = []
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

        return scriptObj

    def run_custem_script(self):
        r = run_cmd(['pgbench', '-f', '/home/susan/PythonClass/django-postgres-stack/client/tmp/files/insert.sql'
                        ,'-f', '/home/susan/PythonClass/django-postgres-stack/client/tmp/files/test.sql', self._dbname],
                    env=self._env)

        # pgbench -b simple-update -h 127.0.0.1 -p 5432 -U postgres TestDB
        # r = run_cmd(['pgbench', '-b', 'simple-update', '-h','127.0.0.1', '-p','5432','-U','postgres',self._dbname],
        #             env=self._env, cwd=self._outdir)
        # r = run_cmd(['pgbench', '--username=postgres', '-i', self._dbname],
        #             env=self._env, cwd=self._outdir)
        # r= os.subprocess.call(["sudo", "-u", "postgres", "pgbench", "-i", self._dbname], stdout=os.subprocess.PIPE)

        return r

    @staticmethod
    def getScriptListJson():
        scriptList = []
        # scriptContent = []
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
            result = json.dumps(scriptList)
            print("collecting self-design script json: " + result)

        else:
            print("collecting self-design script files Error: " + scriptDir + " not exists")

        return scriptList
