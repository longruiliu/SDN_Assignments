'''
Coursera:
- Software Defined Networking (SDN) course
-- Module 4 Programming Assignment

Professor: Nick Feamster
Teaching Assistant: Muhammad Shahbaz
'''

from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr
from collections import namedtuple
import os
''' Add your imports here ... '''
import csv


log = core.getLogger()
policyFile = "%s/pox/pox/misc/firewall-policies.csv" % os.environ[ 'HOME' ]  

''' Add your global variables here ... '''



class Firewall (EventMixin):

    def __init__ (self):
        self.listenTo(core.openflow)
        log.debug("Enabling Firewall Module")

    def _handle_ConnectionUp (self, event):    
        ''' Add your logic here ... '''
        file = csv.reader(open(policyFile))
        for rule in file:
            id,mac1,mac2 = rule
            if id != "id":
                fm = of.ofp_flow_mod()
                fm.match.dl_src = EthAddr(mac1)
                fm.match.dl_dst = EthAddr(mac2)
                event.connection.send(fm)
        log.debug("Firewall rules installed on %s", dpidToStr(event.dpid))

def launch ():
    '''
    Starting the Firewall module
    '''
    core.registerNew(Firewall)
