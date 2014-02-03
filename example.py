import json
from jsonrpclib import Server

switches = ["172.22.28.156", "172.22.28.157", "172.22.28.158"]
username = "admin"
password = "admin"

# Going through all the switch IP addresses listed above
for switch in switches:
    urlString = "https://{}:{}@{}/command-api".format(username, password, switch)
    switchReq = Server( urlString )

    # Display the current vlan list
    response = switchReq.runCmds( 1, ["show vlan"] )
    print "Switch : " + switch + " VLANs: "
    print response[0]["vlans"].keys()

    # Add vlan 100 to the switch
    print "Adding vlan 100"
    response = switchReq.runCmds( 1, ["enable", "configure", "vlan 100"] )

    # List the vlans again to show vlan 100 configured
    response = switchReq.runCmds( 1, ["show vlan"] )
    print "Switch : " + switch + " VLANs: "
    print response[0]["vlans"].keys()


    # Remove vlan 100
    print "Removing vlan 100"
    response = switchReq.runCmds( 1, ["enable", "configure", "no vlan 100"] )
    print
    print
    
