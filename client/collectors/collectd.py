import os
<<<<<<< HEAD
import rrdtool
import os
=======

>>>>>>> d6388beb7f6f23fe6b08843c7c133888b970d3f5
from utils.logging import log
from utils.misc import run_cmd

COLLECTD_CONFIG = '/tmp/.collectd.conf'
COLLECTD_PIDFILE = '/tmp/.collectd.pid'


class CollectdCollector(object):
    """
    Collect basic system and database statistics using collectd.
    """

    def __init__(self, outdir, dbname, bin_path):
        self._bin_path = bin_path

        # Hard code all possible places a packager might install collectd.
        self._env = os.environ
        self._env['PATH'] = ':'.join(['/usr/sbin/', '/sbin/', self._env['PATH']])

        # Assume collectd.conf.in file to be in the same directory as this
        # file.
        cwd = os.path.dirname(os.path.realpath(__file__))

        modules = (
            'LoadPlugin aggregation\n'
            'LoadPlugin contextswitch\n'
            'LoadPlugin cpu\n'
            'LoadPlugin csv\n'
            'LoadPlugin disk\n'
            'LoadPlugin interface\n'
            'LoadPlugin memory\n'
            'LoadPlugin postgresql\n'
            'LoadPlugin processes\n'
            'LoadPlugin swap\n'
<<<<<<< HEAD
	        'LoadPlugin rrdtool\n'
	    

=======
>>>>>>> d6388beb7f6f23fe6b08843c7c133888b970d3f5
        )

        system = os.popen("uname").readlines()[0].split()[0]

        if system == 'Linux':
            modules += (
                'LoadPlugin ipc\n'
                'LoadPlugin vmem\n'
<<<<<<< HEAD
                'LoadPlugin syslog\n'
=======
>>>>>>> d6388beb7f6f23fe6b08843c7c133888b970d3f5
            )

        outdir = '%s/stats' % outdir
        config_template = open('%s/collectd.conf.in' % cwd, 'r')
        config = open(COLLECTD_CONFIG, 'w')
        config.write(config_template.read() % {'database': dbname,
                                               'datadir': outdir,
                                               'modules': modules,
                                               'pguser': self._env['USER']})
        config.close()
        config_template.close()

        # TODO: Use collectd to test config act exit appropriately.

    def start(self):
        log("starting collectd")
        cmd = 'collectd -C %s -P %s' % (COLLECTD_CONFIG, COLLECTD_PIDFILE)
        run_cmd(cmd.split(' '), env=self._env)

    def stop(self):
        log("stopping collectd")
        try:
            pidfile = open(COLLECTD_PIDFILE, 'r')
            pid = pidfile.read().strip()
            run_cmd(['kill', pid])
        except FileNotFoundError:
<<<<<<< HEAD
            print('collectd pid not found - processes may still be running')



    def result(self):
        # with open('/tmp/collectd.json.log') as f:
        #     collectdlog=f.read()
        #
        # return {"collectdlog":collectdlog}
        def getaverage(a):
            b = []
            for i in a[2]:
                for u in i:
                    if u != None:
                        b.append(u)
            return (sum(b) / len(b))

        path = "/var/lib/collectd/rrd/iris-VirtualBox/cpu-0"
        path1 = os.path.join(path, 'cpu-idle.rrd')
        a1 = rrdtool.fetch(path1, "AVERAGE")

        path2 = os.path.join(path, 'cpu-interrupt.rrd')
        a2 = rrdtool.fetch(path2, "AVERAGE")

        path3 = os.path.join(path, "cpu-nice.rrd")
        a3 = rrdtool.fetch(path3, "AVERAGE")

        path4 = os.path.join(path, "cpu-softirq.rrd")
        a4 = rrdtool.fetch(path4, "AVERAGE")

        path5 = os.path.join(path, "cpu-steal.rrd")
        a5 = rrdtool.fetch(path5, "AVERAGE")

        path6 = os.path.join(path, "cpu-system.rrd")
        a6 = rrdtool.fetch(path6, "AVERAGE")

        path7 = os.path.join(path, "cpu-user.rrd")
        a7 = rrdtool.fetch(path7, "AVERAGE")

        path8 = os.path.join(path, "cpu-wait.rrd")
        a8 = rrdtool.fetch(path8, "AVERAGE")

        return{"cpu_idle":str(getaverage(a1)),
               "cpu_interrupt":str(getaverage(a2)),
               "cpu_nice":str(getaverage(a3)),
               "cpu_softirq":str(getaverage(a4)),
               "cpu_steal":str(getaverage(a5)),
               "cpu_system":str(getaverage(a6)),
               "cpu_user":str(getaverage(a7)),
               "cpu_wait": str(getaverage(a8)),
               }
=======
            log('collectd pid not found - processes may still be running')

    def result(self):
        return {}
>>>>>>> d6388beb7f6f23fe6b08843c7c133888b970d3f5


def run_collector(in_queue, out_queue, dbname, bin_path, outdir, interval=1.0):
    pass
