#!/usr/bin/env python
"""
    cpu_stat - Python Module for CPU Stats on Linux


    requires:
    - Python 2.6+
    - Linux 2.6+
"""

import time

def cpu_times():
    """Return a sequence of cpu times.each number in the sequence is
     the amount of time, measured in units of USER_HZ (1/100ths of a
     second on most architectures), that the system spent in each cpu mode:
    (user, nice, system, idle, iowait, irq, softirq, [steal], [guest]).
    """
    with open('/proc/stat') as pf:
        line = pf.readline()

    cpu_times =[int(x) for x in line.split()[1:]]

    return cpu_times

def cpu_info():

    """Return the logical cpu info. On SMP systems, the values are
        representing a single processor. The key processor_count has the number
        of processors
    """
    with open('/proc/cpuinfo') as pf:
        cpuinfo = {'processor_count':0}
        for line in pf:
            if ":" in line:
                fields = line.replace('\t','').strip().split(': ')
                #count processors and filter out main info
                if fields[0] == 'processor':
                    cpuinfo['processor_count'] += 1
                elif fields[0] != 'core_id':
                    try:
                        cpuinfo[fields[0]] = fields[1]
                    except IndexError:
                        pass
        return cpu_info

