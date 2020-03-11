import rrdtool
import os
path="/var/lib/collectd/rrd/iris-VirtualBox/cpu-0"
path1 = os.path.join(path,'cpu-idle.rrd')
a1=rrdtool.fetch(path1,"AVERAGE")



def getaverage(a):
    b=[]
    for i in a[2]:
        for u in i:
            if u != None:
                b.append(u)
    return(sum(b)/len(b))

print(getaverage(a1))

# path2 = os.path.join(path,'cpu-interrupt.rrd')
# a2=rrdtool.fetch(path2,"AVERAGE")
#
# path3 =os.path.join(path, "cpu-nice.rrd")
# a3=rrdtool.fetch(path3,"AVERAGE")
#
# path4 = os.path.join(path,"cpu-softirq.rrd")
# a4=rrdtool.fetch(path4,"AVERAGE")
#
# path5 =os.path.join(path,"cpu-steal.rrd")
# a5=rrdtool.fetch(path5,"AVERAGE")
#
# path6 = os.path.join(path,"cpu-system.rrd")
# a6=rrdtool.fetch(path6,"AVERAGE")
#
# path7 =os.path.join(path,"cpu-user.rrd")
# a7=rrdtool.fetch(path7,"AVERAGE")
#
# path8 = os.path.join(path,"cpu-wait.rrd")
# a8=rrdtool.fetch(path8,"AVERAGE")
