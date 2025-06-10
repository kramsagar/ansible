#!/usr/bin/env python3
import json, socket, re

def extract_hostnames(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return [re.search(r"\{(.+?)\}", line).group(1) for line in lines if "{" in line]

hosts = extract_hostnames("hosts.txt")

data = {
    "all": {"hosts": hosts},
    "_meta": {
        "hostvars": {
            host: {"ansible_host": socket.gethostbyname(host)} for host in hosts
        }
    }
}

print(json.dumps(data))
