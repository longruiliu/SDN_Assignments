'''
Coursera:
- Software Defined Networking (SDN) course
-- Module 3 Programming Assignment

Professor: Nick Feamster
Teaching Assistant: Muhammad Shahbaz
'''

from mininet.topo import Topo
from mininet.util import irange

class CustomTopo(Topo):
    "Simple Data Center Topology"

    "linkopts - (1:core, 2:aggregation, 3: edge) parameters"
    "fanout - number of child switch per parent switch"
    def __init__(self, linkopts1, linkopts2, linkopts3, fanout=2, **opts):
        # Initialize topology and default options
        Topo.__init__(self, **opts)

        # Add your logic here ...
        controller = self.addSwitch('c1')
        #e_num and h_num are the number of edge switch and host
        e_num = 1
        h_num = 1

        for i in irange(1, fanout):
            switch_a = self.addSwitch('a%s' % i)
            for j in irange(1, fanout):
                switch_e = self.addSwitch('e%s' % e_num)
                for k in irange(1, fanout):
                    host = self.addHost('h%s' % h_num)
                    self.addLink(host, switch_e, bw = linkopts3.get('bw'), delay = linkopts3.get('delay'))
                    h_num += 1
                self.addLink(switch_e,switch_a, bw = linkopts2.get('bw'), delay = linkopts2.get('delay'))
                e_num += 1
            self.addLink(switch_a,controller, bw = linkopts1.get('bw'), delay = linkopts1.get('delay'))

topos = { 'custom': ( lambda: CustomTopo() ) }
