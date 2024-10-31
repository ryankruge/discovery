# Discovery (Device Discovery Tool)
Discovery is a device discovery tool that operates via ARP packets that are transmitted across the network. It is quick to deploy and automatically determines which network interfaces you wish to use as well as calculates your subnet mask and its corresponding CIDR notation.
# Application Usage
## Support:
Currently, this tool is supported on both **Windows** and **Linux**.
## Requirements:
- Scapy Library
- JSON Library
```
python -m pip install ./requirements.txt
```
## Summary:
This is an active reconnaissance tool and therefore it can be easily detected on networks that have active monitoring by systems such as an IDS or an administrator. If this tool is required for stealth usage, you should **NOT** use it as it uses broadcast frames which transmit across the entire network until it reaches its destination.