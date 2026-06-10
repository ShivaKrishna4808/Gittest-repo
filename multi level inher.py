class network:
    def connectivity(self):
        return "Network Connects"
    
class Network_5G(network):
    def fast_connectivity(self):
        return "5G Network Provides Superfast Connectivity"
    
class Network_5G_Airtel(Network_5G):
    def fast_and_stable_conectvt(self):
        return "Airtel_5G Network is fast and remains stable"
    
# Network_5G_Airtel
network_obj = Network_5G_Airtel()
print(network_obj.connectivity())

print(network_obj.fast_connectivity())

print(network_obj.fast_and_stable_conectvt())

# network

