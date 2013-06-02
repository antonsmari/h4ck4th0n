#!/usr/bin/env python

import os
import signal
import sys

pids = []

if len(sys.argv) != 2:
	print("missing argument")
	sys.exit(1)

try:
	for x in range(0, int(sys.argv[1])):
		pid = os.fork()
		
		if pid == 0:
			while True:
				pass
		else:
			pids.append(pid)
	
	for x in pids:
		os.waitpid(x, 0)
except KeyboardInterrupt:
	for x in pids:
		os.kill(x, signal.SIGTERM)

