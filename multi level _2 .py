class network:
    def connectivity(self):
        return"Network Connects"
    
class network_5G(network):
    def fast_connectivity(self):
        return "5G network Provides superfast service"
    def connectivity(self):
        return "5G Networks Connects Faster"
    
class network_5G_Airtel(network_5G):
    def fast_and_stable_connectivity(self):
        return "Airtel 5G network is fast and remains stable"
    
network_5G_Airtel

obj1 = network_5G_Airtel()
print(obj1.connectivity())

