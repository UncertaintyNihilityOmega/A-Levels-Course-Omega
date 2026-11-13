# data/cs.ip_expected.py: prints expected values from Python's ipaddress module as JSON,
# for data/cs.ip_test.js to compare with the cs-ip widget's arithmetic.
import ipaddress
import json
import random

random.seed(5)
cases = [("192.168.10.77", 26), ("172.16.37.200", 20), ("10.0.0.5", 8), ("8.8.8.8", 30), ("192.168.40.150", 27),
         ("192.168.1.64", 26), ("192.168.1.127", 26), ("127.0.0.1", 24), ("169.254.3.4", 16), ("172.32.0.1", 12),
         ("172.31.255.255", 12), ("255.1.1.1", 9), ("0.1.2.3", 8)]
for _ in range(300):
    ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    cases.append((ip, random.randint(8, 30)))
out = []
for ip, p in cases:
    n = ipaddress.ip_interface(f"{ip}/{p}").network
    a = ipaddress.ip_address(ip)
    if int(a) >> 24 == 127:
        kind = "loopback"
    elif int(a) >> 16 == (169 << 8) + 254:
        kind = "link-local"
    elif a in ipaddress.ip_network("10.0.0.0/8") or a in ipaddress.ip_network("172.16.0.0/12") or a in ipaddress.ip_network("192.168.0.0/16"):
        kind = "private"
    elif int(a) >> 24 == 0 or int(a) >> 24 >= 224:
        kind = "reserved"
    else:
        kind = "public"
    out.append({"ip": ip, "prefix": p, "network": str(n.network_address), "broadcast": str(n.broadcast_address),
                "first": str(n.network_address + 1), "last": str(n.broadcast_address - 1),
                "hosts": n.num_addresses - 2, "mask": str(n.netmask), "kind": kind})
print(json.dumps(out))
