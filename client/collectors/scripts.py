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
        self._scriptFileList = []
        self.hasScript()



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

    def hasScript(self):
        isHasScript =False
        if os.path.exists(self._dirPath):
            self._scriptFileList = glob.glob(self._dirPath + "/*.sql")
            if(len(self._scriptFileList) > 0):
                isHasScript = True
        return  isHasScript


    def _collect_scriptDir_info(self):
        # scriptList = []
        # scriptContent = []

        for script in self.sqlScript:
            scriptObj = {}
            # fp = open(script, 'r')
            # for line in fp.readlines():
            #     scriptContent.append(line)
            # fp.close()
            # scriptObj["content"] = scriptContent
            scriptObj["scriptName"] = os.path.basename(script)
        #     scriptList.append(scriptObj)
        # json = json.dumps(scriptList)
        # print("collecting self-design script json: " + json)

        return scriptObj

    def run_custem_script(self):
        args = ['pgbench']
        for script in self._scriptFileList:
            print(script)
            args.append('-f')
            path = os.path.abspath(script)
            args.append(path)
        args.append(self._dbname)

        r = run_cmd(args,
                    env=self._env)



        return r

    def getScriptListJson(self):
        scriptList = []
        # scriptContent = []
        for script in self._scriptFileList:
            scriptObj = {}
            scriptObj["scriptName"] = os.path.basename(script)
            scriptList.append(scriptObj)
        result = json.dumps(scriptList)
        print("collecting self-design script json: " + result)


        return scriptList
