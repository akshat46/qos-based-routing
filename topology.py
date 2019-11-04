from mininet.topo import Topo
class MyTopo(Topo):
	"Topology."
	def __init__(self):
		"Creating custom topo."
		Topo.__init__(self)
		Switch1 = self.addSwitch('s1', ip='10.0.1.1')
		Switch2 = self.addSwitch('s2', ip='10.0.2.1')
		Switch3 = self.addSwitch('s3', ip='10.0.3.1')
		Switch4 = self.addSwitch('s4', ip='10.0.4.1')
		Host1 = self.addHost('h11', ip='10.0.1.10')
		Host2 = self.addHost('h21', ip='10.0.2.10')
		Host3 = self.addHost('h31', ip='10.0.3.10')
		Host4 = self.addHost('h41', ip='10.0.4.10')

		self.addLink(Host1, Switch1)
		self.addLink(Host2, Switch2)
		self.addLink(Host3, Switch3)
		self.addLink(Host4, Switch4)

		self.addLink(Switch1, Switch2)
		self.addLink(Switch1, Switch3)
		self.addLink(Switch1, Switch4)
		self.addLink(Switch2, Switch3)
		self.addLink(Switch2, Switch4)
		self.addLink(Switch3, Switch4)
topos = {'mytopo': (lambda: MyTopo())}
