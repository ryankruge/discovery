# Discovery (Device Discovery Tool)
Discovery is a device discovery tool that operates via the use of address resolution (ARP) packets that are transmitted across the network. It is quick to deploy and automatically determines which network card to use. The IP address corresponding to that network interface card is then used to determine the subnet mask in the form of CIDR notation. You can initiate an active scan which actively broadcasts ARP packets asking what devices are on the network, or a passive scan which listens for outgoing ARP packets without broadcasting anything to the rest of the network.
# Application Usage
## Support:
Currently, this tool is supported on both **Windows** and **Linux**. Most functions / libraries used within this application are already cross-platform and therefore only small changes have been needed to support both platforms.
## Requirements:
- Scapy Library
- JSON Library
```
python -m pip install ./requirements.txt
```
## Summary:
This is an active reconnaissance tool and therefore it can be easily detected on networks that have active monitoring by systems such as an IDS or an administrator. If this tool is required for stealth usage, you should **NOT** use it as it uses broadcast frames which transmit across the entire network until it reaches its destination.
