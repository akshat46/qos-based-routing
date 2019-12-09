from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

		# Add hosts and switches
		h1 = self.addHost( 'h1' )
		h2 = self.addHost( 'h2' )
		h3 = self.addHost( 'h3' )
		h4 = self.addHost( 'h4' )
		s1 = self.addSwitch( 's1' )
		s2 = self.addSwitch( 's2' )
		s3 = self.addSwitch( 's3' )
		s4 = self.addSwitch( 's4' )

		# Add links
		self.addLink( h1, s1 )
		self.addLink( h2, s1 )
		self.addLink( s1, s2 )
		self.addLink( s2, h3 )
		self.addLink( s2, h4 )
		# more links between switches
		self.addLink( s1, s3 )
		self.addLink( s3, s2 )
		self.addLink( s3, s4 )
		self.addLink( s2, s4 )
		self.addLink( s4, s1 )
	# changing switch ofp version
#	self.switches['s1'].cmd("ovs-vsctl set bridge s1 protocols=OpenFlow13")
#	self.switches['s2'].cmd("ovs-vsctl set bridge s2 protocols=OpenFlow13")
#	self.switches['s3'].cmd("ovs-vsctl set bridge s3 protocols=OpenFlow13")
#	self.switches['s4'].cmd("ovs-vsctl set bridge s4 protocols=OpenFlow13")

topos = { 'mytopo': ( lambda: MyTopo() ) }

