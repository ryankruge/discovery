#!/usr/bin/python3
# All software written by Tomas. (https://github.com/shelbenheimer)

from scapy.all import ARP, srp, Ether, get_if_addr, conf
from json import load
import time
import sys
import os

BANNER      = "Software written by Tomas. Available on GitHub. (https://github.com/shelbenheimer)"
VENDOR_PATH = "Resources/manuf.json"

class Discovery:
	def __init__(self):
		self.target  = self.FormatAddress(get_if_addr(conf.iface))
		self.path    = f'{os.path.dirname(os.path.abspath(__file__))}/{VENDOR_PATH}'
		self.vendors = self.PopulateVendors()

	def GetHosts(self):
		packet  = Ether(dst="FF:FF:FF:FF:FF:FF") / ARP(pdst=self.target)
		replies = srp(packet, timeout=1, verbose=False)[0]

		if not replies:
			return []

		hosts = []
		for reply in range(0, len(replies)):
			information = (replies[reply][1].psrc, replies[reply][1].hwsrc)
			hosts.append(information)
		return hosts

	def FormatAddress(self, ip):
		mask = "255.255.255.0"

		split_mask = mask.split('.')
		split_addr = ip.split('.')
		counted = 0
		for octet in range(0, len(split_mask)):
			if split_mask[octet] == "0":
				split_addr[octet] = "0"

			binary = bin(int(split_mask[octet]))[2:]
			for digit in binary:
				if digit == '1': counted += 1

		result = f'{".".join(split_addr)}/{counted}'
		return result

	def PopulateVendors(self):
		try:
			with open(self.path, 'r', encoding="utf8") as file:
				vendors = load(file)
				return vendors
		except Exception as error:
			print(error)
			return {}

	def FormatOUI(self, address):
		formatted = address[:8].replace("-", ":")
		return formatted

	def GetVendor(self, address):
		if not self.vendors:
			return "Unobtainable"

		try:
			formatted = self.FormatOUI(address).upper()
			return self.vendors[formatted]
		except:
			return "Unknown Vendor"

def Main():
	try:
		print(BANNER)
		
		discovery = Discovery()
		if not discovery.PopulateVendors():
			print("Failed to populate manufacturer database.")

		print(f'Commencing scan on {discovery.target} on {time.ctime()}.')
		start_time = time.time()
		hosts = discovery.GetHosts()
		if not hosts:
			print("There was an error whilst attempting to scan the network.")
			return

		for host in hosts:
			vendor = discovery.GetVendor(host[1])
			print(f'{host[0]:<18} {host[1]:<20} {vendor:<20}')

		elapsed = time.time() - start_time
		formatted_elapsed = "".join(list(str(elapsed))[:5])
		print(f'Finished scan in {formatted_elapsed}s.')
	except Exception as error:
		print(error)
		return

if __name__ == "__main__": Main()