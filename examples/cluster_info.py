#!/usr/local/bin/python2.7

from pythonlsf import lsf

print '\n Hosts in cluster: ', lsf.get_host_names()

print '\n Clustername: ', lsf.ls_getclustername(), '\n'

print '{0:15s} {1:20s} {2:20s} {3:5s} {4:4s}'.format('Hostname', 'Type',
                                                     'Model', 'Cores', 'Load')

for info in lsf.get_host_info():

    load = lsf.get_host_load("hname=" + info.hostName, lsf.R15M)
    if load >= 65535:
        load = -1

    print '{0:15s} {1:20s} {2:20s} {3:5d} {4:4.2f}'.format(info.hostName,
                                                           info.hostType,
                                                           info.hostModel,
                                                           info.cores,
                                                           load)

    if info.nRes > 0:
        print ' +--> Resources:', info.resources
