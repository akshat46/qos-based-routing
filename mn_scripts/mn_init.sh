echo "************CLEANING PREVIOUS TOPOLOGY*************"
eval "sudo mn -c"
echo "****************CREATING TOPOLOGY******************"
eval "sudo mn --controller=remote,ip=$1 --custom=topology.py --topo=mytopo --switch=ovsk,protocol=OpenFlow13"
