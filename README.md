# Discovery (Network Device Discovery Tool)
Discovery is a network device discovery and analysis tool that operates via the use of **Address Resolution Protocol** (ARP) packets that are *optionally* broadcasted across the network. It is quick to deploy and automatically determines which network card to use. You can initiate an active scan which actively broadcasts ARP packets across the network, or launch a passive scan to passively listen for outgoing ARP packets——a much stealthier option for detection avoidance, but takes longer.
# Installation
## Guide
1. If not already installed, install [PipX](https://pipx.pypa.io/stable/installation/).
2. In the root directory of the application, execute `pipx install .`
3. After the installation has completed, ensure that `~/.local/bin` is added to PATH.
# Application Usage
## Support
This application was written in Python, and therefore supports Windows, Linux, and MacOS.
## Requirements
- Scapy Library
- [Npcap](npcap.com/#download) (Windows)
## Summary
This is a reconnaissance tool which, if used incorrectly, will be detected by networks with basic security measures in place. The use of this software should be kept within the bounds of local and federal laws and regulations. I will not accept responsibility for any repercussions incurred by such misuse.