import glob
import os.path

from datetime import datetime, timedelta, time
from utils.logging import log
from utils.misc import run_cmd


class ScriptCollector(object):
    'Collect various Linux-specific statistics (cpuinfo, mounts)'

    def __init__(self, scriptdirpath):
        self._dirPath = scriptdirpath



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
        scriptObj = {}
        scriptContent = []
        scriptDir = self._dirPath
        if os.path.exists(scriptDir):
            sqlScript = glob.iglob(scriptDir + "/*.sql")

            for script in sqlScript:
                fp = open(script, 'r')
                for line in fp.readlines():
                    scriptContent.append(line)
                fp.close()
                scriptObj["content"] = scriptContent
                scriptObj["scriptName"] = script
            # json = json.dumps(scriptObj)
            # print("collecting self-design script json: " + json)

        else:
            print("collecting self-design script files Error: " + scriptDir + " not exists")

        return scriptObj
