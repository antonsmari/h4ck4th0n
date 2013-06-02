#!/usr/bin/python
from _socket import socket
from boto.ec2.regioninfo import RegionInfo
from boto.ec2.connection import EC2Connection

import socket
import commands 
import os
import sys
import random

from time import time,sleep
from pprint import pprint

from config import *

class GreenQloudSimpleTest:

	def create_connection(self, pub_key=ec2_public_key, pri_key=ec2_private_key):
		"""
		Returns a boto ec2 connection for the current environment.
		"""
		region = RegionInfo(name=ec2_region, endpoint=ec2_uri)
		return EC2Connection(aws_access_key_id=pub_key,
								aws_secret_access_key=pri_key,
								is_secure=ec2_is_secure,
								host=ec2_uri,
								path=ec2_path,
								port=ec2_port,
								region=region)

	def setUp(self):
		self.conn = self.create_connection(pub_key=ec2_public_key,
										   pri_key=ec2_private_key)
		self.data = {}
		return self.conn

	def tearDown(self):
		pass
		
			
	def create_server(self):
		reservation = self.conn.run_instances('qmi-f2a9d2ba',key_name='QWERTY', instance_type='t1.nano')
		#reservations = self.conn.get_all_instances()
		#instances = [i for r in reservations for i in r.instances]
		#pprint(reservations[0].__dict__)
		#for ins in instances:
			#print(str(ins) + " || -_- || " + ins.value)
			#pprint(ins.__dict__)
			
	def list_servers(self):
		reservations = self.conn.get_all_instances()
		instances = [i for r in reservations for i in r.instances]
		#pprint(instances[0].__dict__)
		return instances
		
	def testing(self):
		pprint(self.conn.__dict__)
		
if __name__ == '__main__':
	test = GreenQloudSimpleTest()
	test.setUp()
	pprint(test.list_servers()[0].__dict__)