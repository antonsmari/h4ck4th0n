#!/usr/bin/env python

import GQASB
import pystache
import yaml
import os
import sys
from pprint import pprint

config = yaml.load(open(sys.argv[1]))

machines = {
	"instances" : [
		#{
		#	"value"      : "crap23",
		#	"public_ip"  : "46.149.18.7",
		#	"private_ip" : "10.1.1.139",
		#},
		#{
		#	"value"      : "i-c46401a4",
		#	"public_ip"  : "46.149.23.148",
		#	"private_ip" : "10.1.1.133",
		#},
	],
}

test = GQASB.GreenQloudSimpleTest()
test.setUp()

if sys.argv[2] == "CRITICAL" and sys.argv[3] == "HARD":
	test.create_server()

servers = test.list_servers()

for server in servers:
	if server.id not in config["ignore-instances"]:
		if server.state == "running":
			machines["instances"].append({
				"value"      : server.id,
				"public_ip"  : server.ip_address,
				"private_ip" : server.private_ip_address,
			})

for template in config["templates"]:
	render = pystache.render(open(template["template"]).read(), machines)
	
	handler = open(template["location"], "w+b")
	handler.write(render)
	handler.close()
	
for command in config["commands"]:
	os.system(command)

