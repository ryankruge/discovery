#!/usr/bin/python3
# All software written by Tomas. (https://github.com/ryankruge)

from scapy.all import ARP, srp, Ether, get_if_addr, conf, sniff
from json import load
import time
import sys
import os

BANNER           = "Software written by Tomas. Available on GitHub. (https://github.com/ryankruge)"
VENDOR_PATH      = "Resources/manuf.json"

HELP_DIALOGUE = """-h | Displays this dialogue, a debug menu describing the behaviour of flags within this program.
-p | Enables passive scan mode which listens rather than actively broadcasting to discover hosts.
-d | Sets the duration in which the passive scan mode will operate for. This flag is optional."""

PASSIVE_STATUS   = False
DEFAULT_DURATION = 30

class Discovery:
	def __init__(self):
		self.target  = self.FormatAddress(get_if_addr(conf.iface))
		self.path    = f'{os.path.dirname(os.path.abspath(__file__))}/{VENDOR_PATH}'
		self.vendors = self.PopulateVendors()

	def ActiveDiscovery(self):
		packet  = Ether(dst="FF:FF:FF:FF:FF:FF") / ARP(pdst=self.target)
		replies = srp(packet, timeout=1, verbose=False)[0]

		if not replies:
			return []

		hosts = []
		for reply in range(0, len(replies)):
			information = (replies[reply][1].psrc, replies[reply][1].hwsrc)
			hosts.append(information)
		return hosts

	def PassiveDiscovery(self, duration):
		discovered_hosts = {}

		def ProcessPacket(packet):
			if packet.haslayer(ARP):
				ip = packet[ARP].psrc
				mac = packet[ARP].hwsrc
				if (ip, mac) not in discovered_hosts:
					vendor = self.GetVendor(mac)
					print(f'{ip:<18} {mac:<20} {vendor:<20}')
					discovered_hosts[(ip, mac)] = vendor

		sniff(filter="arp", prn=ProcessPacket, store=0, timeout=duration)

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

def ParseArguments(arguments, parameters):
	populated_parameters = parameters
	for argument in range(0, len(arguments)):
		match arguments[argument]:
			case '-h':
				print(HELP_DIALOGUE)
				sys.exit()
			case '-d':
				parameters['Duration'] = int(arguments[argument + 1])
			case '-p':
				parameters['Passive'] = True
	return populated_parameters

def main():
	try:
		print(BANNER)
		
		argument_parameters = { 'Passive': PASSIVE_STATUS, 'Duration': DEFAULT_DURATION }
		ParseArguments(sys.argv, argument_parameters)

		discovery = Discovery()
		if not discovery.PopulateVendors():
			print("Failed to populate manufacturer database.")

		if argument_parameters['Passive']:
			print(f'Commencing passive scan on {discovery.target} on {time.ctime()} for {argument_parameters['Duration']} second(s).')
			discovery.PassiveDiscovery(argument_parameters['Duration'])
			sys.exit()

		print(f'Commencing active scan on {discovery.target} on {time.ctime()}.')
		start_time = time.time()

		hosts = discovery.ActiveDiscovery()
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
