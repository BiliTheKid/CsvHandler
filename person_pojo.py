
class Person:
    def __init__(self,id , mac , dns):
        self.id = id
        self.mac = mac
        self.dns  = dns
        self.arr_dns=[]

    def add_to_dns(self,dns):
        self.arr_dns.append(dns)
        #self.dns=self.arr_dns

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_mac(self):
        return self.mac

    def set_mac(self, mac):
        self.mac = mac

    def get_dns(self):
        return self.dns

    def set_dns(self, dns):
        self.dns= dns

    def get_arr_dns(self):
        return self.arr_dns
