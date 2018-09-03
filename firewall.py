import csv
import ipaddress
from pprint import pprint


def check_ip(rule_ip, test_ip):
    if "-" in rule_ip:
        h = rule_ip.find("-")
        range_ = (int(ipaddress.ip_address(rule_ip[:h])), int(ipaddress.ip_address(rule_ip[h + 1:])))
        return int(ipaddress.ip_address(range_[0])) <= int(ipaddress.ip_address(test_ip)) <= int(
            ipaddress.ip_address(range_[1]))
    else:
        return int(ipaddress.ip_address(rule_ip)) == int(ipaddress.ip_address(test_ip))


def check_port(p1, p2):
    if "-" in p1:
        h = p1.find("-")
        range_ = (int(p1[:h]), int(p1[h + 1:]))
        return range_[0] <= p2 <= range_[1]
    else:
        return int(p1) == int(p2)


class Firewall(object):
    stream = {}

    def __init__(self, path):
        # avoid repitive calls
        self.stream["inbound"] = {}
        self.stream["outbound"] = {}
        self.stream["inbound"]["tcp"] = {}
        self.stream["inbound"]["udp"] = {}
        self.stream["outbound"]["tcp"] = {}
        self.stream["outbound"]["udp"] = {}
        print(self.stream)

        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                print(row)
                present_ports = self.stream[row[0]][row[1]]
                if row[3] in present_ports:
                    pprint([row[3]])
                    self.stream[row[0]][row[1]][row[2]] += [row[3]]
                else:
                    self.stream[row[0]][row[1]][row[2]] = [row[3]]

    def accept_packet(self, dir, pro, por, ips):

        if self.stream[dir][pro] is not None:
            port = self.stream[dir][pro]

        for port_num, ip in port.items():

            if check_port(port_num, por):
                for ipadd in ip:
                    if check_ip(ipadd, ips):
                        return True
        return False


fw = Firewall('/Users/brentrobinson/PycharmProjects/illumio/rules.csv')
print(fw.stream)

print(fw.accept_packet("inbound", "tcp", 80, "192.168.1.2"))
print(fw.accept_packet("inbound", "udp", 53, "192.168.2.1"))
print(fw.accept_packet("outbound", "tcp", 10234, "192.168.10.11"))
print(fw.accept_packet("inbound", "tcp", 81, "192.168.1.2"))
print(fw.accept_packet("inbound", "udp", 24, "52.12.48.92"))
print(fw.accept_packet("outbound", "tcp", 63, "221.192.199.70"))
