import glob
import os.path
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



    def hasScript(self):
        isHasScript =False
        if os.path.exists(self._dirPath):
            self._scriptFileList = glob.glob(self._dirPath + "/*.sql")
            if(len(self._scriptFileList) > 0):
                isHasScript = True
        return  isHasScript


    def _collect_scriptDir_info(self):


        for script in self.sqlScript:
            scriptObj = {}
            scriptObj["scriptName"] = os.path.basename(script)


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
        for script in self._scriptFileList:
            scriptObj = {}
            scriptObj["scriptName"] = os.path.basename(script)
            scriptList.append(scriptObj)
        result = json.dumps(scriptList)
        print("collecting self-design script json: " + result)
        return scriptList
