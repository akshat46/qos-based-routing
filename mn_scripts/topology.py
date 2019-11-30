# from mininet.topo import Topo
# class MyTopo(Topo):
# 	"Topology."
# 	def __init__(self):
# 		"Creating custom topo."
# 		Topo.__init__(self)
# 		s1 = self.addSwitch('s1', ip='10.0.1.1')
# 		s2 = self.addSwitch('s2', ip='10.0.2.1')
# 		s3 = self.addSwitch('s3', ip='10.0.3.1')
# 		s4 = self.addSwitch('s4', ip='10.0.4.1')
# 		h11 = self.addHost('h11', ip='10.0.1.10')
# 		h21 = self.addHost('h21', ip='10.0.2.10')
# 		h31 = self.addHost('h31', ip='10.0.3.10')
# 		h41 = self.addHost('h41', ip='10.0.4.10')

# 		self.addLink(h11, s1)
# 		self.addLink(h21, s2)
# 		self.addLink(h31, s3)
# 		self.addLink(h41, s4)

# 		self.addLink(s1, s2)
# 		self.addLink(s1, s3)
# 		self.addLink(s1, s4)
# 		self.addLink(s2, s3)
# 		self.addLink(s2, s4)
# 		self.addLink(s3, s4)
# topos = {'mytopo': (lambda: MyTopo())}

#!/usr/bin/python

import sys
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.node import RemoteController
from mininet.node import OVSKernelSwitch
from mininet.log import setLogLevel

class CreateTopo( Topo ):
    "Single switch connected to n hosts."
    def build( self, n=4 ):
        s1 = self.addSwitch('s1', ip='10.0.0.1')
        s2 = self.addSwitch('s2', ip='10.0.0.2')
        s3 = self.addSwitch('s3', ip='10.0.0.3')
        s4 = self.addSwitch('s4', ip='10.0.0.4')
        h11 = self.addHost('h11', ip='10.0.0.11')
        h21 = self.addHost('h21', ip='10.0.0.21')
        h31 = self.addHost('h31', ip='10.0.0.31')
        h41 = self.addHost('h41', ip='10.0.0.41')
        
        self.addLink(h11, s1)
        self.addLink(h21, s2)
        self.addLink(h31, s3)
        self.addLink(h41, s4)

        self.addLink(s1, s2)
        self.addLink(s1, s3)
        self.addLink(s1, s4)
        self.addLink(s2, s3)
        self.addLink(s2, s4)
        self.addLink(s3, s4)

#To enable the stp setting for the switches of the topology
def enableSTP(switches):
	for s in switches:
		s.cmd("ovs-vsctl set bridge " + s.name + " stp_enable=true")

#To print the stp setting of the switches in the topology
def printSTPSetting(switches):
	for s in switches:
		print(s.cmd("ovs-vsctl get bridge " + s.name + " stp_enable"))

def perfTest():
    "Create network and run simple performance test"
    IP = sys.argv[1]
    print "Ip of the controller is: " + IP
    topo = CreateTopo( n=4 )
    net = Mininet( topo=topo, controller=lambda name: RemoteController('c1', ip=IP, port=6633), switch=OVSKernelSwitch)
    # ~ c1 = net.addController('c1', controller=RemoteController, ip=IP, port=6653)
    c1 = net.controllers[0]
    c1.start()
    net.start()
    print "Dumping host connections"
    dumpNodeConnections( net.hosts )
    print "Testing network connectivity"
    net.pingAll()
    # print "Testing bandwidth between h1 and h4"
    # h1, h4 = net.get( 'h1', 'h4' )
    # net.iperf( (h1, h4) )
    # net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    perfTest()
